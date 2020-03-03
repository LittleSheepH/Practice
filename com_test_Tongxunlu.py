# coding=utf-8
import pandas as pd
import json
from common.confDB import MysqlDB
from common.confHttp import postRisk, get
from common.expectjson_new import ExtractJson


# work=xlrd.open_workbook(r'E:\demo\testCase\风控标签\TagType.xlsx','r')
# sheet=work.sheet_by_index(0)

def test_gambling(userId):
    print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用户" + userId + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    type_list = ['telephone', 'normalPhone', 'kinshipShortPhone', 'publicServicePhone', 'noteContainSensitiveWordPhone',
                 'noteContainLoansNumberPhone','containIntermediaryAgentNumberPhone','hasKnAccountPhone','hasSsjAccountPhone','hasLoansRecordPhone'
                 ,'hasOverdueRecordPhone']

    # 获取数据到风控库里
    myapi=json.loads(doget(userId))
    requestId = ExtractJson().extract_json_value(myapi,'data.requestId')[0]
    yunYingShang= ExtractJson().extract_json_value(myapi,'data.运营商通话详单')[0]
    baichengtongxunluudid= ExtractJson().extract_json_value(myapi,'data.BaiChengUdid')[0]
    BaiChengtonghuajiluUdid= ExtractJson().extract_json_value(myapi,'data.BaiChengCallogsUdid')[0]

    # 获取接口数据
    d = dopost(userId)
    allPhoneCategory = ExtractJson().extract_json_value(d,'info.allPhoneCategory')

    # 创建数据库连接
    db1 = MysqlDB('test_risk_db_conf')
    db1.conn()
    # 电话
    telephoneNumber_sql = """
                            select min(userid),min(userName),phoneValue from
                            (
                            select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'  and udid = '#{udid}' and contacts_type = 'phone'
                            union all
                            select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}' ) tt
                            where  LENGTH(phoneValue) = 11  and phoneValue REGEXP '^[1](3[0-9]|4[57]|5[012356789]|6[6]|7[035678]|8[0-9]|9[89])[0-9]{8}$'
                            group by  phoneValue"""
    telephoneNumber_sql =telephoneNumber_sql.replace('%s',userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)
    # 座机
    normalPhoneNumber_sql="""select min(userid),min(userName),phoneValue from
                            (
                            select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'  and udid = '#{udid}' and contacts_type = 'phone'
                            UNION all
                            select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}' ) tt
                            where  LENGTH(phoneValue) >=7 and    LENGTH(phoneValue) <=12
                            and phoneValue not REGEXP '^[1](3[0-9]|4[57]|5[012356789]|6[6]|7[035678]|8[0-9]|9[89])[0-9]{8}$'
                            group by  phoneValue"""
    normalPhoneNumber_sql = normalPhoneNumber_sql.replace('%s',userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)
    # 亲情短号
    kinshipShortPhoneNumber_sql="""select min(userid),min(userName),phoneValue  from
                            (
                            select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'  and udid = '#{udid}'  and contacts_type = 'phone'
                            UNION all
                            select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s'  and requestId = '#{requestId}'  ) tt
                            where  LENGTH(phoneValue) <= 6
                            and phoneValue  not  in (select commen_service as  phoneValue from test.dim_tongxunlu where commen_service is not null )
                            group by  phoneValue"""
    kinshipShortPhoneNumber_sql = kinshipShortPhoneNumber_sql.replace('%s',userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)
    # 公共服务电话
    publicServicePhoneNumber_sql="""select min(userid),min(userName),phoneValue  from
                                (
                                select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'  and udid ='#{udid}' and contacts_type = 'phone'
                                UNION all
                                select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}' ) tt
                                where   phoneValue   in (select commen_service as  phoneValue from test.dim_tongxunlu where commen_service is not null )
                                group by  phoneValue"""
    publicServicePhoneNumber_sql = publicServicePhoneNumber_sql.replace('%s',userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)
    # 命中贷款业务敏感词
    noteContainSensitiveWordPhoneNumber_sql="""select min(userid),min(userName),phoneValue,min(sensitives) from
                                (
                                select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'  and udid ='#{udid}'   and contacts_type = 'phone'
                                UNION all
                                select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}' ) tt
                                JOIN
                                 (SELECT sensitives FROM test.dim_tongxunlu WHERE sensitives IS NOT NULL AND sensitives <> '') t
                                on  tt.userName like  CONCAT('%',t.sensitives,'%')
                                group by  phoneValue"""
    noteContainSensitiveWordPhoneNumber_sql = noteContainSensitiveWordPhoneNumber_sql.replace('%s',userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)
    # 命中贷款平台词
    noteContainLoansNumberPhoneNumber_sql="""select * from (
                                select min(userid) as userid  ,min(userName) as userName,phoneValue from
                                (
                                select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'   and udid = '#{udid}'  and contacts_type = 'phone'
                                UNION all
                                select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}' ) t1
                                group by  phoneValue ) tt
                                JOIN
                                 (select loan from test.dim_tongxunlu where loan is not null AND loan <> '')  t
                                on  tt.userName like  CONCAT('%',t.loan,'%')"""
    noteContainLoansNumberPhoneNumber_sql = noteContainLoansNumberPhoneNumber_sql.replace('%s',userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)
   # 命中中介电话
    containIntermediaryAgentNumberPhoneNumber_sql = """select * from (select min(userid),min(userName),phoneValue from
                                (
                                select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'   and udid = '#{udid}'    and contacts_type = 'phone'
                                UNION all
                                select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}') tt
                                where    phoneValue  in (select userkn_rc_phone as  phoneValue  from test.t_risk_phone_library_test  where userkn_rc_phone is not null and userkn_rc_is_agent_user = 1 )
                                group by  phoneValue) t """
    containIntermediaryAgentNumberPhoneNumber_sql = containIntermediaryAgentNumberPhoneNumber_sql.replace('%s', userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)

    # 有卡牛账户号码
    hasKnAccountPhoneNumber_sql = """select min(userid),min(userName),phoneValue from
                                    (
                                    select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'   and udid = '#{udid}'   and contacts_type = 'phone'
                                    UNION all
                                    select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}') tt
                                    where    phoneValue  in (select userkn_rc_phone as  phoneValue  from test.t_risk_phone_library_test  where userkn_rc_phone is not null and userkn_rc_is_agent_user = 1 )
                                    group by  phoneValue """
    hasKnAccountPhoneNumber_sql = hasKnAccountPhoneNumber_sql.replace('%s', userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)

    # 有随手记账户号码
    hasSsjAccountPhoneNumber_sql = """select min(userid),min(userName),phoneValue from
                                       (
                                       select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'   and udid = '#{udid}'   and contacts_type = 'phone'
                                       UNION all
                                       select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}') tt
                                       where    phoneValue  in (select userkn_rc_phone as  phoneValue  from test.t_risk_phone_library_test  where userkn_rc_phone is not null and userkn_rc_ssj_register_user = 1 )
                                       group by  phoneValue"""
    hasSsjAccountPhoneNumber_sql = hasSsjAccountPhoneNumber_sql.replace('%s', userId).replace('#{requestId}',requestId).replace('#{udid}', baichengtongxunluudid)

    # 有贷款放款记录的号码
    hasLoansRecordPhoneNumber_sql = """select min(userid),min(userName),phoneValue from
                                       (
                                       select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'   and udid = '#{udid}'   and contacts_type = 'phone'
                                       UNION all
                                       select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}') tt
                                       where    phoneValue  in (select userkn_rc_phone as  phoneValue  from test.t_risk_phone_library_test  where userkn_rc_phone is not null and userkn_rc_loan_user = 1 )
                                       group by  phoneValue """
    hasLoansRecordPhoneNumber_sql = hasLoansRecordPhoneNumber_sql.replace('%s', userId).replace('#{requestId}',requestId).replace('#{udid}', baichengtongxunluudid)

    # 有逾期记录的号码
    hasOverdueRecordPhoneNumber_sql = """select min(userid),min(userName),phoneValue from
                                       (
                                       select userId,userName,phoneValue  from risk_data.t_user_contacts_phone where userId ='%s'   and udid = '#{udid}'   and contacts_type = 'phone'
                                       UNION all
                                       select userid,name as userName ,value as phoneValue from test.db_datacenter_callogs_info  where  userId ='%s' and requestId = '#{requestId}') tt
                                       where    phoneValue  in (select userkn_rc_phone as  phoneValue  from test.t_risk_phone_library_test  where userkn_rc_phone is not null and userkn_rc_m3_user = 1 )
                                       group by  phoneValue """
    hasOverdueRecordPhoneNumber_sql = hasOverdueRecordPhoneNumber_sql.replace('%s', userId).replace('#{requestId}', requestId).replace('#{udid}', baichengtongxunluudid)

    yunYIngshang_tonghuaTime="""select count(phoneValue)as  cntphoneValue ,IFNULL(sum(callDuration),0.0)  as  sumphoneValue from
                            (#{tpye_templet}) ta1
                            join
                            (select * from test.db_operator_user_bill_call_list  where requestId ='#{request}') ta2
                            on  ta1.phoneValue =  ta2.otherSidePhone
                            #{day_param} """

    day7=""" where callTime  >= date_sub(curdate(), INTERVAL 7 DAY)  and  callTime < date_sub(curdate(), INTERVAL 0 DAY) """
    day60 = """ where callTime  >= date_sub(curdate(), INTERVAL 60 DAY)  and  callTime < date_sub(curdate(), INTERVAL 0 DAY) """
    day90=""" where callTime  >= date_sub(curdate(), INTERVAL 90 DAY)  and  callTime < date_sub(curdate(), INTERVAL 0 DAY) """
    dayall=""
    maxday="""select ifnull(max(cntphoneValue),0) as cntphoneValue ,ifnull(max(sumphoneValue+0),0)  as sumphoneValue FROM ( #{minmax}  GROUP BY phoneValue ) a """

    for i in range(len(type_list)):
        type_str = type_list[i]
        phoneCategoryNumber = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.phoneCategoryNumber','info.allPhoneCategory.type', type_str)
        my7dayesult = yunYIngshang_tonghuaTime.replace('#{tpye_templet}',locals()[type_list[i]+'Number_sql']).replace('#{request}',requestId).replace('#{day_param}',day7)
        my30dayesult = yunYIngshang_tonghuaTime.replace('#{tpye_templet}',locals()[type_list[i]+'Number_sql']).replace('#{request}',requestId).replace('#{day_param}',day60)
        my90dayesult = yunYIngshang_tonghuaTime.replace('#{tpye_templet}',locals()[type_list[i]+'Number_sql']).replace('#{request}',requestId).replace('#{day_param}',day90)
        myalldayesult = yunYIngshang_tonghuaTime.replace('#{tpye_templet}',locals()[type_list[i]+'Number_sql']).replace('#{request}',requestId).replace('#{day_param}',dayall)
        maxdayesult=maxday.replace("#{minmax}",myalldayesult)
        type_str = type_list[i]
        sevenDaysCallTimes = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.sevenDaysCallTimes','info.allPhoneCategory.type', type_str)
        sevenDaysCallDuration = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.sevenDaysCallDuration','info.allPhoneCategory.type', type_str)
        thirtyDaysCallTimes = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.thirtyDaysCallTimes','info.allPhoneCategory.type', type_str)
        thirtyDaysCallDuration = ExtractJson().extract_lookup_json_value(d,'info.allPhoneCategory.thirtyDaysCallDuration','info.allPhoneCategory.type', type_str)
        ninetyDaysCallTimes = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.ninetyDaysCallTimes','info.allPhoneCategory.type', type_str)
        ninetyDaysCallDuration = ExtractJson().extract_lookup_json_value(d,'info.allPhoneCategory.ninetyDaysCallDuration','info.allPhoneCategory.type', type_str)
        allCallTimes = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.allCallTimes','info.allPhoneCategory.type', type_str)
        allCallDuration = ExtractJson().extract_lookup_json_value(d,'info.allPhoneCategory.allCallDuration','info.allPhoneCategory.type', type_str)
        maxCallTimes = ExtractJson().extract_lookup_json_value(d, 'info.allPhoneCategory.maxCallTimes','info.allPhoneCategory.type', type_str)
        maxCallDuration = ExtractJson().extract_lookup_json_value(d,'info.allPhoneCategory.maxCallDuration','info.allPhoneCategory.type', type_str)

        # 类别号码个数
        sql = locals()[type_list[i] + 'Number_sql']
        sql = """ select count(1)  as cnt from ( """ + sql + """ )ttt"""
        numbersql_result = pd.read_sql(sql=sql, con=db1.db)
        numberesult = numbersql_result.to_dict('index')[0]['cnt']
        varname = ' ' + type_str + ' 的phoneCategoryNumber'
        mynumberesult = 'NULL' if (numberesult == 0  and  phoneCategoryNumber is None)   else numberesult
        myphoneCategoryNumber = 'NULL' if phoneCategoryNumber is None else phoneCategoryNumber
        compare(userId, varname, mynumberesult, myphoneCategoryNumber)
        # 30天通话次数和通话时长
        test(db1,my7dayesult,userId,type_str,sevenDaysCallTimes,sevenDaysCallDuration,"sevenDaysCallTimes","sevenDaysCallDuration")
        # 7天通话次数和通话时长
        test(db1,my30dayesult,userId,type_str,thirtyDaysCallTimes,thirtyDaysCallDuration,"thirtyDaysCallTimes","thirtyDaysCallDuration")
        # 90天通话次数和通话时长
        test(db1,my90dayesult,userId,type_str,ninetyDaysCallTimes,ninetyDaysCallDuration,"ninetyDaysCallTimes","ninetyDaysCallDuration")
        # 总通话次数和通话时长
        test(db1,myalldayesult,userId,type_str,allCallTimes,allCallDuration,"allCallTimes","allCallDuration")
        # 最高次数和通话时长
        test(db1,maxdayesult,userId,type_str,maxCallTimes,maxCallDuration,"maxCallTimes","maxCallDuration")


def test(db1,sql, user_id,type_str, DaysCallTimes, DaysCallDuration,varname1,varname2 ):
        DaysCallTimes_result = pd.read_sql(sql=sql, con=db1.db)
        mydaycntsultresult = DaysCallTimes_result.to_dict('index')[0]['cntphoneValue']
        mydaysumsultresult = DaysCallTimes_result.to_dict('index')[0]['sumphoneValue']
        varname = ' ' + type_str + '  的 '+varname1
        varname1 = ' ' + type_str + ' 的 '+varname2
        cnt30 = 'NULL' if  (mydaycntsultresult == 0   and  DaysCallTimes is None) else mydaycntsultresult
        apicnt30 = 'NULL' if DaysCallTimes is None else DaysCallTimes
        sum30 = 'NULL' if (mydaysumsultresult == 0.0  and  DaysCallDuration is None)  else mydaysumsultresult
        apisum30 = 'NULL' if DaysCallDuration is None else DaysCallDuration
        compare(user_id, varname, cnt30, apicnt30)
        compare(user_id, varname1, sum30, apisum30)


def compare(UserId, Var, myresult, apiresult):
    if str(myresult) == str(apiresult):
        print("用户user====" + UserId + "的" + Var + "变量:测试通过=========变量值：" + str(myresult))
    else:
        print("用户user====" + UserId + "的" + Var + "变量：测试失败------------------------------------------------------------- 我的变量值:" + str(
            myresult) + ",接口变量值:" + str(apiresult))


def dopost(userId):
    url = 'http://10.201.7.209:8444/variable-web/variable/address'
    body = {
        'userId': '%s' % str(userId),
        'productCode': 'baixinyinhang'
    }
    r = postRisk(url=url, body=body)
    print(r.text)
    d = r.json()
    return d

def doget(userId):
    url = 'http://localhost:8078/txl/yunyingshang.do'
    param = {
          'reKnUserId' :' %s'  %userId
    }
    r = get(url=url, param=param)
    return r


test_gambling("15340922749")

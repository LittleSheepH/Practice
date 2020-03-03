# -*-coding:utf-8-*-
# @Time       :2018/12/23 7:59
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :database_plus_1.py
# @Software   :PyCharm
from api_auto_class.common.request import Request
from api_auto_class.common.mysql_con import MysqlUtil
from api_auto_class.common.doexcel import readcase
from api_auto_class.common import concants
import re
import json
import pymysql

sql = "select mobilephone from future.member where mobilephone != ''order by mobilephone desc limit 1 "
connect = MysqlUtil()
get = connect.fetch_one(sql)
print(get)
max=int(get['mobilephone'])+1
print(max)
patten='\$\{.*?\}'


filename=readcase(concants.data)
cases=filename.get_case('register')
url='http://120.78.128.25:8080/futureloan/mvc/api/member/register'
data='{"mobilephone":"${register}","pwd":"1234567890","regname":"huihui"}'

print("初始的data:------------------------",data)
mobile=re.findall(patten,data)

aa=data.replace(mobile[0],str(max))
print("替换后的data,赋值给aa-----------------------",aa)
print("aa的类型",type(aa))

res=Request(method='get',url=url,data=eval(aa))
print(res.get_json())
connect = MysqlUtil()
get = connect.fetch_one(sql)
print(get)

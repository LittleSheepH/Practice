# -*-coding:utf-8-*-
# @Time       :2019/11/13 23:19
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :SF_test.py
# @Software   :PyCharm
import pymysql
import re
sqa="select sum(s.cnt) from student_info.new_cnt s right join  student_info.city_code t on s.code=t.send where s.current_date='2019-11-13' "
sqa1="select sum(s.cnt) from student_info.new_cnt s join  student_info.city_code t on s.code=t.send " \
     "where s.current_date='2019-11-13' and t.area_code='${code}'"
mysql = pymysql.connect(host='localhost', user='root', password="123456",port=3306)#cursorclass=)
cursor=mysql.cursor()
cursor.execute(sqa)
a = cursor.fetchall()
print(a)
sqa2="select area_code from student_info.city_code "
cursor1=mysql.cursor()
cursor1.execute(sqa2)
b = cursor1.fetchall()
print(b,type(b),b[0][0],len(b))
patten = '\$\{(.*?)\}'
res=re.findall(patten,sqa1)
# print(res)
List=['755R','888Y']
for i in b:
    print(i[0])
    res1 = re.sub(patten,i[0],sqa1)
    cursor2 = mysql.cursor()
    cursor2.execute(res1)
    c = cursor2.fetchall()
    s=str(c)+str(i[0])+'\n'
    print(c,i[0])
    f1 = open('C:\python_code\Practice\key1.txt', 'a')
    f1.write(s)


mysql.close()

# sql1 = "select mobilephone from future.member"
# cursor1=mysql.cursor()
# cursor1.execute(sql1)
# b =cursor1.fetchmany(3)
s1='{"mobilephone":"${register}","pwd":"${password},"regname":"huihui"}'
patten = '\$\{(.*?)\}'
patten1='\$\{.*?\}'
res=re.findall(patten,s1)
# res1= re.sub(patten,'s1',s1)
c='112345'
for i in res:
    for j in range(len(c)):
        res1= re.sub(patten,c[j],s1,count=1)
        # print(res1)
# print(res)
# -*-coding:utf-8-*-
# @Time       :2018/12/24 23:13
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :fetch_one.py
# @Software   :PyCharm
import pymysql
import re
sql = "select mobilephone from future.member where mobilephone != ''order by mobilephone desc limit 1 "
mysql = pymysql.connect(host='120.78.128.25', user='futurevistor', password="123456",port=3306)#cursorclass=)
cursor=mysql.cursor()
cursor.execute(sql)
a = cursor.fetchall()
sql1 = "select mobilephone from future.member"
cursor1=mysql.cursor()
cursor1.execute(sql1)
b =cursor1.fetchmany(3)
s1='{"mobilephone":"${register}","pwd":"${password},"regname":"huihui"}'
patten = '\$\{(.*?)\}'
patten1='\$\{.*?\}'
res=re.findall(patten,s1)
# res1= re.sub(patten,'s1',s1)
c='112345'
for i in res:
    for j in range(len(c)):
        res1= re.sub(patten,c[j],s1,count=1)
        print(res1)
print(res)


# -*-coding:utf-8-*-
# @Time       :2019/10/31 22:51
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :列表推导式.py
# @Software   :PyCharm
#表达式 for 变量 in 序列或迭代对象
import os

aList=[x*x for x in range(10)]
print(aList)
#1、使用列表推导式实现嵌套列表的平铺
a=[[1,2,3],[4,5,6],[7,8,9]]
aa=[i for x in a for i in x]
print(aa)
print([filename for filename in os.listdir('.')if filename.endswith('.py')])
b=[1,2,3,4,5,6]
b1=[i for i in b]

#2、从下列列表中取出符合条件的列表组成新列表
c=[-1,3,4,7,10,-10,9]
#取出所有大于3的数字组成新的列表
c1=[i for i in c if i>3]
#3、已知有一个包含同学成绩的字典，计算最高分，最低分，平均分，并找出分数最高的同学
scores={"zhang":45,"Li":50,"wang":100,"zhao":98,"haha":76}
print(max(scores.values()))
highest=max(scores.values())
print(min(scores.values()))
avg=sum(scores.values())/len(scores)
print(avg)
highestperson=[name for name,score in scores.items() if score==highest]
print(highestperson)
a={}
for name,score in scores.items():
    if score==highest:
        a[name]=score
        print(a)
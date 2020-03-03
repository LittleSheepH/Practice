# -*-coding:utf-8-*-
# @Time       :2019/6/13 21:48
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :面试题.py
# @Software   :PyCharm
# com.tencent.qqmusic/.activity.AppStarterActivity

from   collections.abc import Iterable
a="666"
b=True
LIST__mylist=[1,2,3,4]
#假设字符串"abacaba",里面包括4个'a',2个'b',1个'c',于是这个字符串的价值为4 * 4 + 2 * 2 + 1 * 1 = 21
# s=input("请输入一个字符串：")
# sum=0
# for i in set(s):
#     c=s.count(i)
#     value=int(c*c)
#     sum+=value
# print(sum)

#
def getInfo(abc,a,b):
    startIndex = abc.index(a)
    if startIndex>=0:
        startIndex+=len(a)
        endIndex=abc.index(b)
        print(startIndex)
        print(endIndex)
        print(abc[0:startIndex-4])
        return abc[startIndex:endIndex]
print(getInfo('terlet is good jobs','er','od'))
with open("LR.txt",'a')as fs:
    for i in range(0000,10000):
        new_num ="test"+(4-len(str(i)))*"0"+str(i)
        fs.write(new_num)
        fs.write("\n")


# -*-coding:utf-8-*-
# @Time       :2019/7/27 21:56
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :去首尾字符.py
# @Software   :PyCharm
str = "abcdef"

x = str.strip(str[0] + str[-1])
print(x)
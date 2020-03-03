# -*-coding:utf-8-*-
# @Time       :2019/6/24 20:15
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :request学习.py
# @Software   :PyCharm

import requests
url="https://www.baidu.com/"
def Request(self,url,method):
    res=requests.get(url)
    print(res)
    res1=requests.post(url)
    print(res1)
def http_request(url,param,http_method,cook=None):
    if http_method=="get":
        res=requests.get(url,param,cookies=cook)
    else:
        res=requests.post(url,param)
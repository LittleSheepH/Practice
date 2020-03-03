# -*-coding:utf-8-*-
# @Time       :2019/12/3 23:48
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :post_man.py
# @Software   :PyCharm
import requests

url = "https://postman-echo.com/time/before"

querystring = {"timestamp":"2018-06-20","target":"2018-08-23"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "44a41cda-357a-4440-8a19-9ab6f716c5ef"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
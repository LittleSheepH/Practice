# -*-coding:utf-8-*-
# @Time       :2019/6/30 23:18
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :天彩-加密解密.py
# @Software   :PyCharm
import string
import random
from binascii import b2a_hex, a2b_hex
import requests

#c:\python_code\futureloan\venv\lib\site-packages文件夹下crypto文件改名，没错，就是直接改成Crypto
# pip3 install -i https://pypi.douban.com/simple pycryptodome 直接安装，便可正常使用该模块
from Crypto.Cipher import AES

url='http://blc.smartlight.qmulux-demo.com:8080/cloud/common/app/user/security/getRegisterCode'
data= '"<getCode version=“1.0” xmlns=”urn:skylight”><mobile >XXX</mobile><areaCode >XXX</areaCode></getCode>'
# res=requests.post(url,data)
# print(res)
#生成指定长度的秘钥
def keyGenerater(length):
    if length not in (16,24,32):
        return None
    x=string.ascii_letters+string.digits
    return ''.join([random.choice(x)for i in range(length)])
def encryptor_decryptor(key,mode):
    return AES.new(key,mode, b'qqqqqqqqqqqqqqqq')

#加密
def AESencrypt(key,mode,text):
    encryptor=AES.new(key,mode, b'qqqqqqqqqqqqqqqq')
    return encryptor.encrypt(text)
#解密
def AESdecrypt(key,mode,text):
    # 解密后，去掉补足的空格用strip() 去掉

    decryptor=encryptor_decryptor(key,mode)
    return decryptor.decrypt(text)
if __name__ == '__main__':

    text='wangwangwangwangqqqqqqqq'
    key=keyGenerater(16)
    print(key)
    mode=AES.MODE_CBC
    print(mode)
    print("加密前的字符串",text)

    text_encoded=text.encode()
    text_length=len(text_encoded)
    padding_length=16-text_length%16
    # text = text + ('\0' * add).encode('utf-8')
    text_encoded=text_encoded+b'0'*padding_length
    print(text_encoded)

    text_encrypted=AESencrypt(key,mode,text_encoded)
    print("kkkkkkkkkkkkkkkkkk")
    print("加密后",text_encrypted)

    text_decrypted=AESdecrypt(key,mode,text_encrypted)
    print("解密后",text_decrypted.decode()[:-padding_length])



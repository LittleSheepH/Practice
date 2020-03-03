# -*-coding:utf-8-*-
# @Time       :2019/7/1 14:00
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :jiami.py
# @Software   :PyCharm
import time

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import datetime
import requests
class PrpCrypt(object):

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        # self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串

        return b2a_hex(cryptor.encrypt(text))

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    key_pre = datetime.datetime.now().strftime('%d%H%M%S')
    key = str(key_pre + 'skylight')
    print(key)
    pc = PrpCrypt(key)  # 初始化密钥
    e = pc.encrypt("12345678")  # 加密
    print(e)
    d = pc.decrypt(e)
    print(d)# 解密
    url="http://blc.smartlight.qmulux-demo.com:8080/cloud/common/app/user/security/userRegister"
    data='<appNewUser version ="1.0" xmlns ="urn:skylight">' \
         '<email>1185771797@qq.com</email>' \
         '<dateTime>2019-07-01T17:02:09+08:00</dateTime>' \
         '<encodePw>{}</encodePw>' \
         '<firstName>Wang I</firstName>' \
         '<lastName>ddd</lastName>' \
         '<areaCode></areaCode></appNewUser>'.format(e)

    data_encode=pc.encrypt(data)

    res=requests.post(url,data)
    print(res.text)
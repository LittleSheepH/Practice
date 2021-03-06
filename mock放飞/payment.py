# -*- coding:utf-8 -*-
'''
create by 放飞 on 2019/1/5
function:支付类
'''

import requests

class Payment:
    def requestOutOfSystem(self, card_num, amount):
        url = 'http://thrid.payment.pay/'
        data = {"card_num":card_num, "ammount":amount}
        res = requests.post(url, data=data, timeout=10)
        return res.status_code

    def doPay(self,user_id, card_num, amount):
        try:
            result = self.requestOutOfSystem(card_num, amount)
        except TimeoutError:
            result = self.requestOutOfSystem(card_num, amount)

        if result == 200:
            print("{0}支付{1}成功,并进行扣款".format(user_id, amount))
            return 'success'
        elif result == 500:
            print("{0}支付{1}失败,不进行扣款".format(user_id, amount))
            return 'fail'
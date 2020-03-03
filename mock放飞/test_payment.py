# -*- coding:utf-8 -*-
'''
create by 放飞 on 2019/1/5
function:测试支付类
'''

import unittest
from unittest import mock
from unittest.mock import call
from mock放飞.payment import Payment


class TestPayment(unittest.TestCase):
    def setUp(self):
        self.payment = Payment()

    def test_success(self):
        #mock模拟payment实例中的requestOutOfSystem方法的返回值
        self.payment.requestOutOfSystem = mock.Mock(return_value = 200)
        res = self.payment.doPay('user_001', '111111111', 1000)
        self.assertEqual('success', res, '调用支付接口成功')

    def test_fail(self):
        #mock模拟payment实例中的requestOutOfSystem方法的返回值
        self.payment.requestOutOfSystem = mock.Mock(return_value = 500)
        res = self.payment.doPay('user_002', '22222222', 200000)
        self.assertEqual('fail', res, '调用支付接口失败')

    def test_retry_success(self):
        #side_effect模拟时动态返回值，第一次调用返回第一个值，第n次调用返回第n个值，可以返回异常，返回的值必须为可迭代对象
        #优先级比return_value,当return_value与side_efeect同时存在时，side_effect会覆盖return_value的值
        self.payment.requestOutOfSystem = mock.Mock(return_value=500, side_effect =[TimeoutError, 200])
        res = self.payment.doPay('user_003', '33333333', 300000)
        self.assertEqual('success', res, '超时再次调用支付接口成功')
        #断言模拟的行为调用的参数是否正确
        self.payment.requestOutOfSystem.assert_called_with('33333333', 300000)
        self.assertEqual(2, self.payment.requestOutOfSystem.call_count) #断言被调用的次数


    def test_retry_fail(self):
        self.payment.requestOutOfSystem = mock.Mock(side_effect =[TimeoutError, 500])
        res = self.payment.doPay('user_004', '4444444444', 400000)
        self.assertEqual('fail', res, '超时再次调用支付接口失败')
        # 断言模拟的行为调用的参数是否正确
        self.payment.requestOutOfSystem.assert_called_with('4444444444', 400000)

        fooCalls = [call('4444444444',400000)]
        self.payment.requestOutOfSystem.assert_has_calls(fooCalls)  # 检查mock对象是否按照正确的顺序和参数调用

    def tearDown(self):
        print("模拟的行为是否被调用",self.payment.requestOutOfSystem.called)
        print("模拟的行为最近一次被调用的参数", self.payment.requestOutOfSystem.call_args)
        print("模拟的行为被调用的参数列表", self.payment.requestOutOfSystem.call_args_list)
        print("模拟的行为被调用的次数", self.payment.requestOutOfSystem.call_count)

if __name__ == '__main__':
    unittest.main()
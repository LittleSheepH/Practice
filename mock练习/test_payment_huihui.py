# -*-coding:utf-8-*-
# @Time       :2019/6/23 22:53
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :test_payment_huihui.py
# @Software   :PyCharm
import unittest
from mock练习.payment import Payment
from unittest import mock

class TestPayment(unittest.TestCase):
    def setUp(self):
        self.pay=Payment()
    #正确的用户信息，正确的返回
    def test_01_success(self):
        #模拟paymanet返回200
        self.pay.requestOutOfSystem=mock.Mock(return_value=200)
        res=self.pay.doPay(1,'1234567', 10000)
        self.assertEqual('success',res,'测试正确支付')
    #正确的用户信息，错误的返回
    def test_02_fail(self):
        self.pay.requestOutOfSystem=mock.Mock(return_value=500)
        res=self.pay.doPay(2,'2334545',100)
        self.assertEqual('fail',res,"测试支付失败")
    #timeout重试，之后返回正确的信息
    def test_03_retry_success(self):
        self.pay.requestOutOfSystem=mock.Mock(side_effect=[TimeoutError,200])
        res = self.pay.doPay(3, '3334545', 100)
        self.assertEqual('success', res, '重试后测试正确支付')
        #断言模拟参数是否正确
        self.pay.requestOutOfSystem.assert_called_with('3334545', 100)
        print(self.pay.requestOutOfSystem.assert_called_with('3334545', 100))
        fooCalls = [mock.call('3334545', 100)]
        self.pay.requestOutOfSystem.assert_has_calls(fooCalls)  # 检查mock对象是否按照正确的顺序和参数调用
    #timeout重试，返回错误的信息
    def test_04_retry_fail(self):
        self.pay.requestOutOfSystem = mock.Mock(side_effect=[TimeoutError, 500])
        res = self.pay.doPay(4, '4334545', 100000)
        self.assertEqual('fail', res, '重试后测试支付失败')
        #断言模拟参数是否按顺序d调用
        self.pay.requestOutOfSystem.assert_has_calls([mock.call('4334545', 100000)])
        #断言模拟参数调用次数是否为2
        self.assertEqual(2,self.pay.requestOutOfSystem.call_count)
        #断言模拟参数是否正确
        self.pay.requestOutOfSystem.assert_called_with('4334545', 100000)
    def tearDown(self):
        print('mock对象是否被调用',self.pay.requestOutOfSystem.called)
        print('mock对象被调用的次数',self.pay.requestOutOfSystem.call_count)
        print("获取最近调用时使用的参数",self.pay.requestOutOfSystem.call_args)
        print("获取工厂调用时的所有参数【列表】",self.pay.requestOutOfSystem.call_args_list)
        print("测试当前mock对象都调用了哪些方法",self.pay.requestOutOfSystem.method_calls)
        print("----------------------------------------------------------------------------------")

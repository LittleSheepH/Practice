# -*-coding:utf-8-*-
# @Time       :2019/6/24 0:04
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :test_payment_antospec.py
# @Software   :PyCharm
import unittest
from mock练习.payment import Payment1
from unittest import mock

class TestPayment(unittest.TestCase):
    def setUp(self):

        # 有时候需要模拟一个函数或者类的行为，包括它所有的属性和方法，如果手动去一个个添加，实在低效而且容易出错。
        # mock提供了autospec的功能，根据提供的模板类生成一个mock实例
        self.fooOperation = mock.create_autospec(Payment1, return_value=None)
        # op=mock.create_autospec(需要模拟类的类名，返回值自定义)
        # self.Payment = self.fooOperation
    #正确的用户信息，正确的返回
    def test_01_success(self):
        # self.fooOperation.
        self.fooOperation.requestOutOfSystem.return_value = 200
        print(self.fooOperation.requestOutOfSystem)
        self.fooOperation.doPay.return_value = 200

        #模拟paymanet返回200

    # def tearDown(self):
    #     print('mock对象是否被调用',self.pay.requestOutOfSystem.called)
    #     print('mock对象被调用的次数',self.pay.requestOutOfSystem.call_count)
    #     print("获取最近调用时使用的参数",self.pay.requestOutOfSystem.call_args)
    #     print("获取工厂调用时的所有参数【列表】",self.pay.requestOutOfSystem.call_args_list)
    #     print("测试当前mock对象都调用了哪些方法",self.pay.requestOutOfSystem.method_calls)
    #     print("----------------------------------------------------------------------------------")

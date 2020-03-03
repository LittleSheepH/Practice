# -*- coding:utf-8 -*-
'''
create by 放飞 on 2019/1/5
function:mock整个类
'''
import unittest
from unittest import mock
from mock放飞.operation import Operation
from unittest.mock import patch

class TestOperation(unittest.TestCase):
    def setUp(self):
        #有时候需要模拟一个函数或者类的行为，包括它所有的属性和方法，如果手动去一个个添加，实在低效而且容易出错。
        # mock提供了autospec的功能，根据提供的模板类生成一个mock实例
        self.fooOperation = mock.create_autospec(Operation, return_value=None)
        self.operation = self.fooOperation

    # def test_add(self):
    #     self.operation.add = self.fooOperation.add
    #     self.fooOperation.add.return_value = 8
    #     print(self.fooOperation.add)
    #     result = self.operation.fun(1,2)
    #     self.assertEqual(result, 8)
    #     self.fooOperation.add.assert_called_with(1,2)

    def test_add(self):
        self.operation.add.return_value = 8
        print(self.operation.add)
        result = self.operation.add(1,2)
        self.assertEqual(result, 8)

    def tearDown(self):
        print("测试当前mock对象都调用了哪些方法", self.operation.method_calls)

if __name__ == '__main__':
    unittest.main()
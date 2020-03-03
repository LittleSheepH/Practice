# -*- coding:utf-8 -*-
'''
create by 放飞 on 2019/1/5
function:解决测试依赖
'''

import unittest
from mock放飞.operation import Function
from unittest.mock import patch

class TestFunction(unittest.TestCase):
    def setUp(self):
        pass

    '''我们要测试A模块，然后A模块依赖于B模块的调用。但是，由于B模块的改变，导致了A模块返回结果的改变，
    从而使A模块的测试用例失败。其实，对于A模块，以及A模块的用例来说，并没有变化，不应该失败才对'''

    # patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试。在测试过程中，您指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原。
    #在定义测试用例中，将mock的multiply()函数（对象）重命名为 mock_multiply对象
    @patch("operation.Function.multiply")
    def test_add_and_multiply(self,mock_multiply):
        x = 3
        y = 5
        #设定mock_multiply对象的返回值为固定的15。
        mock_multiply.return_value = 15
        addition, multiple = Function().add_and_multiply(x, y)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)
        # 检查ock_multiply方法的参数是否正确
        mock_multiply.assert_called_once_with(3, 5)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
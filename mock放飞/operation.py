# -*- coding:utf-8 -*-
'''
create by 放飞 on 2019/1/5
function:算术运算
'''

class Operation:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        pass

    def multi(self, a, b):
        return a*b

class Function:
    # def multiply(self, x, y):
    #     return x * y

    def multiply(self, x, y):
        return x * y+3

    def add_and_multiply(self, x, y):
        addition = x + y
        multiple = self.multiply(x, y)
        return (addition, multiple)


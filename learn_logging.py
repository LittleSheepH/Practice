# -*-coding:utf-8-*-
# @Time       :2018/12/29 19:15
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :learn_logging.py
# @Software   :PyCharm
import logging

logger = logging.getLogger('huihui')
logger.setLevel('DEBUG')
#默认输出warning信息
# root logger 是系统自定义的手机日志的收集器
#handles输出渠道，默认输出到控制台
formatter = '%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s'
form= logging.Formatter(formatter)
#z指定自己的渠道
ch = logging.StreamHandler()
ch.setLevel('DEBUG')
ch.setFormatter(form)

fh = logging.FileHandler('log.txt',encoding='utf-8')
fh.setLevel('INFO')#包括INFO 闭区间
fh.setFormatter(form)

logger.addHandler(fh)
logger.addHandler(ch)
logger.debug('这是一个debug信息')
logger.info('这是一个info信息')
logger.warning('这是一个warning信息')
logger.error('这是一个error信息')
logger.critical('这是一个critica信息')
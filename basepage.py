# -*-coding:utf-8-*-
# @Time       :2019/7/26 19:07
# @Autor      :DAN HUI
# @Email      :1185771797@qq.com
# @File       :basepage.py
# @Software   :PyCharm
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import win32gui
import win32con
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5):
        try:
            #获取开始等待的时间
            StartTime=datetime.now()
            WebDriverWait(self.driver, timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
            EndTime=datetime.now()
            TotalTime=(EndTime-StartTime).microseconds/1000
            print(TotalTime)
        except:
            print("等待元素超时")
            raise
    #查找元素
    def get_element(self,loctor):
        try:
            ele=self.driver.find_element(*loctor)
            print("元素查找成功")
            return ele
        except:
            print("查找元素失败")
            raise
    #点击元素
    def click_element(self,loctor):
        #元素查找
        ele=self.get_element(loctor)
        try:
            ele.click()
        except:
            raise

    #输入内容
    def input_text(self,loctor,text):
        ele = self.get_element(loctor)
        try:
            ele.send_keys(text)
        except:
            print("输入失败")
            raise
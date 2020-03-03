# -*-coding:utf-8-*-
# @Time       :2019/7/26 18:14
# @Autor      :DAN HUI
# @Email      :11857717972@qq.com
# @File       :UI testing.py
# @Software   :PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basepage import BasePage
import unittest

    #等待搜索框可见
driver = webdriver.Chrome()
driver.get('https://www.amazon.cn/dp/B06X3TTC1M/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%9D%AF%E5%AD%90&qid=1564226492&s=gateway&sr=8-1')
driver.maximize_window()

ss=(By.XPATH,'//input[@id="add-to-cart-button"]')
print('测试测试')
WebDriverWait(driver,30,0.5).until(EC.visibility_of_element_located(ss))
print("找到购物车按钮")
driver.find_element(*ss).click()




        # search_input=(By.XPATH,'//input[@type="text"]')
        # search_button=(By.XPATH,'//input[@type="submit"]')
        # WebDriverWait(driver,30,0.5).until(EC.visibility_of_element_located(search_button))
        # driver.find_element_by_xpath('//input[@type="text"]').send_keys("软件测试")
        # driver.find_element_by_xpath('//input[@type="submit"]').click()
        #
        # # BasePage(self.driver).wait_eleVisible(search_input)
        # #输入搜索内容“软件测试”
        # # Click “软件测试（原书第2版）"
        # book_locator='//span[text()="软件测试实战：微软技术专家经验总结 (图灵原创)"]'
        # WebDriverWait(driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,book_locator)))
        # driver.find_element_by_xpath(book_locator).click()

        # Click "加⼊购物⻋" at “软件测试（原书第2版）” page

        # Assert that text "商品已加⼊购物⻋" appears
        # Assert that book price is "20.40"



# -*-coding:utf-8-*-
# @Time       :2019/12/3 22:46
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :test_unit001.py
# @Software   :PyCharm
import time
import  unittest
import  pymysql
from selenium import webdriver
class TestQX(unittest.TestCase):


    def test_001(self):
        self.driver= webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.mysql=pymysql.connect(host='localhost',port=3306,user='root',password="123456",cursorclass=pymysql.cursors.DictCursor)
        cur=self.mysql.cursor()
        sqa = "select area_code from student_info.city_code "
        cur.execute(sqa)
        result=cur.fetchall()
        print(result)
        print(result[0]["area_code"])


        time.sleep(2)
        res=self.driver.find_element_by_xpath('//p[@class="title"]').text
        print(res)
        self.assertEqual('下载百度APP',res,"测试成本中心是否正确")


if __name__ == '__main__':
    unittest.main()
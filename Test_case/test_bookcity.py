import unittest
from commonfun import phoneinfo
from commonfun.log import logging
import time
from appium import webdriver
class Bookcity(unittest.TestCase):
    def setUp(self):
        pass
    def test_book(self):
        logging.info('开始安装app')
        phoneinfo.test_phone()
        time.sleep(10)






    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


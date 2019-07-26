# import unittest
#
#
# class Bookcity(unittest.TestCase):
#     def setUp(self):
#         pass
#     def test_book2(self):
#         pass
#     def tearDown(self):
#         pass
#
# if __name__ == '__main__':
#     unittest.main()


# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 上午10:10
# @Author  : WangJuan
# @File    : test_case.py
import allure
import pytest


@allure.feature('test_module_01')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 1+1 == 3


@allure.feature('test_module_02')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
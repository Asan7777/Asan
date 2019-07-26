import pytest

import allure

#allure:https://www.cnblogs.com/xiaoxi-3-/p/9492534.html
# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
# allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
#@allure.severity:测试用例的重要级别

@allure.feature('test_module_01')
@allure.severity('blocker')
@allure.step('测试书架')
@allure.issue('干什么用的')
@allure.testcase('不知道')
#test_case_01 用例tittle
def test_case_01():
    '''
    用例描述：这是用例描述，出现在什么位置
    '''
    assert 1 + 1 == 3

@allure.feature('test_module_02')
@allure.severity('critical')
#serverity严重级别的定义
# 1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
# 2、 Critical级别：临界缺陷（ 功能点缺失）
# 3、 Normal级别：普通缺陷（数值计算错误）
# 4、 Minor级别：次要缺陷（界面错误与UI需求不符）
# 5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
def test_case_02():
    assert 1 + 3 == 4

@allure.feature('test_module_03')
@allure.story('test_story_01')

def test_case_03():
    assert  1 == 1


if __name__== "__main__":
    pass
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
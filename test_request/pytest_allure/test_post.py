import pytest

import allure

#Feature: 标注主要功能模块
#Story: 标注Features功能模块下的分支功能
#Severity: 标注测试用例的重要级别
#Step: 标注测试用例的重要步骤
#Issue和TestCase: 标注Issue、Case，可加入URL

@allure.feature('test_module_01')
@allure.severity('critical')
#test_case_01 用例tittle
def test_case_01():
    '''
    用例描述：这是用例描述，出现在什么位置
    '''
    assert 1 + 1 == 3

@allure.feature('test_module_02')
@allure.severity('blocker')
def test_case_02():
    assert 1 + 3 == 4

if __name__== "__main__":
    pass
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
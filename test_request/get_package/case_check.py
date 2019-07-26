import json
import operator as op

# from idna import unicode
from idna import unicode


class  CommonUtil():


    def __init__(self, str_one, str_two):
        self.str_one = str_one
        self.str_two = str_two

    def is_contain(self):
        '''
        判断一个字符串是否再另外一个字符串中
        str_one:查找的字符串
        str_two：被查找的字符串
        '''

        #if isinstance(str_one,unicode):
            #str_one = str_one.encode('unicode-escape').decode('string_escape')
            #op.eq 判断俩个字符串是否相等
        #return op.eq(str_one, str_two)
        if self.str_one in self.str_two:
            print(True)
        else:
            print(False)



    def is_equal_dict(self, dict_one, dict_two):
        #isinstance如果对象的类型与参数的类型相同则返回 True，否则返回 False
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return print(dict_one, dict_two)


c = CommonUtil('w','ww')
c.is_contain()


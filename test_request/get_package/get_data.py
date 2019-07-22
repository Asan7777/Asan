
from get_package.Excel_read import OperationExcel
from get_package.json_test import OperetionJson
from get_package.Excel_info import Global_val

class GetData():
    def __int__(self):
        self.open_excel = OperationExcel()

    #获取excel的行数，也就是case的个数
    def get_case_lines(self):
        return self.open_excel.get_lines()



    # 获取请求方式
    def get_request_method(self, row):
        col = int(Global_val.get_request_way())
        request_method = self.open_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = int(Global_val.get_url())
        url = self.open_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(Global_val.get_params())
        data = self.open_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data



    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = int(Global_val.get_expect())
        expect = self.open_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect


    #
    # def write_result(self, row, value):
    #     col = int(Global_val.get_result())
    #     self.open_excel.write_value(row, col, value)


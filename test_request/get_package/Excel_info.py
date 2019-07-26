
# from get_package.get_test import RunMenthod
# from get_package.Excel_info import Global_val





class Global_val:
    # 编号
    Id = '0'
    # 模块名
    request_name = '1'
    # 请求URL
    url = '2'
    # 请求方式
    request_way = '3'
    # 请求参数
    params = '4'
    # 实际结果
    result = '5'
    # 实际结果
    expect = '6'

    @staticmethod
    def get_id():
        return Global_val.Id

    @staticmethod
    def get_request_name():
        return Global_val.request_name

    @staticmethod
    def get_url():
        return Global_val.url

    @staticmethod
    def get_request_way():
        return Global_val.request_way

    @staticmethod
    def get_params():
        return Global_val.params

    @staticmethod
    def get_expect():
        return Global_val.expect

    @staticmethod
    def get_result():
        return Global_val.result

print(Global_val.get_url())


# # r = RunMenthod
# # g = Global_val


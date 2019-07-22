import requests
import json

# from urllib3.util import url


class RunMenthod():
    #封装post请求
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,header=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()
    #封装get请求
    #verify=False  免去ssl认证
    def get_main(self,url,data,header=None,verify=False):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,header=header,verify=False)
        else:
            res =requests.get(url=url,data=data,verify=False)
        return res
    #调用请求
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == "post":
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.jumps(res,ensure_ascii=False)


r=RunMenthod()
r.run_main("get")
import os
import json
import requests
import urllib.request




def ding_talk():
    data = []
    #if判断包名从而确定应用名称
    title = '【接口自动化运行结果通知】 ' + 'Jenkin接口测试运行完成，测试报告已发至邮箱请查收'
    data.append(title)
    # for i in a:
    #     #get_txt从html中提取文本
    #     data.append(i.get_text())
    post_url = 'https://oapi.dingtalk.com/robot/send?access_token=678d04d82e5a7a65405fea7fc36dac4e9e1d2ce75c44a38c8894391d78a5ffe5'
    headers = {'Content-Type': 'application/json'}
    data =  {
    "msgtype": "text",
     "text": {
         "content": data
     }
    }
    #json.dunps将对象编码成json对象
    requests.post(post_url, data=json.dumps(data), headers=headers)


ding_talk()
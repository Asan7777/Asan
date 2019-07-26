import os
import json
import requests
import urllib.request
from bs4 import BeautifulSoup
from commonfun.apkinfo import ApkInfo, apk_path

apk_seat = apk_path()   #获取APK位置
apk_package = ApkInfo(apk_seat).get_apk_pkg()   #获取APK包名
apk_version_name = ApkInfo(apk_seat).get_apk_versionname()   #得到versionName版本
apk_version_code = ApkInfo(apk_seat).get_apk_versioncode()   #得到versionCode版本

def ding_talk():
    # 找到最新html的文件
    new_files = []
    result_html = ( 'D:\\TestAppium'+ '/all_script/' + apk_package + '/report/html_result/')
    lists = os.listdir(result_html)
    # os.path.gettmtime获取文件的最后修改时间
    lists.sort(key=lambda fn: os.path.getmtime(result_html + '/' + fn)
    #判断是否是文件
    if not os.path.isdir(result_html + '/' + fn) else 0)
    #获取最新.htnl的文件
    new_file = os.path.join(result_html, lists[-1])
    #添加到new_files
    new_files.append(new_file)
    #BeautifulSoup转换编码格式
    soup = BeautifulSoup(open(new_file , encoding='UTF-8'), 'lxml')
    #查找.html文件中的标签    #find()查找第一个匹配结果出现的地方，find_all()找到所有匹配结果出现的地方
    a = soup.find_all('p', class_="attribute")
    data = []
    #if判断包名从而确定应用名称
    title = '【自动化运行结果通知】 ' + '应用名称:TXT全本免费小说   ,'+  'APK包名:'+ apk_package+ '   ,versionName版本'+ apk_version_name + '   ,versionCode版本:'+ apk_version_code +'   ,自动化脚本运行完成，测试报告已发送到QQ邮箱请查收'
    data.append(title)
    for i in a:
        #get_txt从html中提取文本
        data.append(i.get_text())
    post_url = 'https://oapi.dingtalk.com/robot/send?access_token=b86f80fb35970f01c0a35225180170dbd6c7b0ae709af215faa135305972ce24'
    headers = {'Content-Type': 'application/json'}
    data =  {
    "msgtype": "text",
     "text": {
         "content": data
     }
    }
    #json.dunps将对象编码成json对象
    requests.post(post_url, data=json.dumps(data), headers=headers)


#ding_talk()
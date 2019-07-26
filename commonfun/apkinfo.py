import os
from math import floor



def apk_path():
    #os.path.dirname(__file__)  去掉文件名 返回目录
    local_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径
    # 获取APP文件夹下的.apk文件
    new_list = []
    items = os.listdir(local_path + '\\Test_app\\')
    for names in items:
        # endswith 判断以什么结尾
        # str.endswith(suffix[, start[, end]])
        if names.endswith(".apk"):
            new_list.append(names)
            file = local_path + '\\Test_app\\' + new_list[0]
    return file  # 输出APK路径

#print(apk_path())

class ApkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath

    # 得到app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkpath) / (1024 * 1000))
        #print(str(size) + "M")
        return str(size) + "M"

    # 得到包名
    def get_apk_pkg(self):
        cmd = 'aapt dump badging ' + self.apkpath + '| find "versionName"'  # 可以直接在命令行中执行的命令
        r = os.popen(cmd)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        for line in info:  # 按行遍历
            line = line.strip('\r\n')
        results = []
        for n in line.split("'"):
            results.append( n )
        result = results[1]
        return (result)

    # 得到versionName版本
    def get_apk_versionname(self):
        cmd = 'aapt dump badging ' + self.apkpath + '| find "versionName"'  # 可以直接在命令行中执行的命令
        r = os.popen(cmd)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        for line in info:  # 按行遍历
            line = line.strip('\r\n')
        results = []
        for n in line.split("'"):
            results.append(n)
        result = results[5]
        return (result)

    # 得到versionCode版本
    def get_apk_versioncode(self):
        cmd = 'aapt dump badging ' + self.apkpath + '| find "versionName"'  # 可以直接在命令行中执行的命令
        r = os.popen(cmd)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        for line in info:  # 按行遍历
            line = line.strip('\r\n')
        results = []
        for n in line.split("'"):
            results.append(n)
        result = results[3]
        return (result)

    # 得到启动类
    def get_apk_activity(self):
        cmd = 'aapt dump badging ' + self.apkpath + ' | find "launchable-activity"'
        r = os.popen(cmd)  # 执行该命令
        info = r.readlines()  # 读取命令行的输出到一个list
        for line in info:  # 按行遍历
            line = line.strip('\r\n')
        results = []
        for n in line.split("'"):
            results.append(n)
        result = results[1]
        return (result)


apk_set = apk_path()
apkinfo = ApkInfo(apk_set).get_apk_versionname()
print(apkinfo)





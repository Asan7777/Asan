import os
import subprocess
from commonfun import apkinfo

#安装获取到的安装包
def installApk():
    apk_seat = apkinfo.apk_path()
    cmd = 'adb install '+ apk_seat
    # print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
    						stderr=subprocess.PIPE,
    						stdin=subprocess.PIPE, shell=True)
    p.communicate()


import logging
import os, sys, time
from commonfun.apkinfo import ApkInfo, apk_path

apk_seat = apk_path()   #获取APK位置
apk_package = ApkInfo(apk_seat).get_apk_pkg()   #获取APK包名
LOCALPATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径
file_time = '%s'%time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))   #获取当前系统时间
Log_FileName = LOCALPATH + '\\all_script\\'+ apk_package + '\\report\\log_result\\'+ file_time + "运行日志报告logs.txt"   #创建日志报告文档
# print('日志存放位置：%s'%Log_FileName)

'''打印到TXT文档日志'''
logging.basicConfig(level=logging.INFO,
				format='[%(asctime)s] [line:%(lineno)d] [%(levelname)s] %(message)s',
				datefmt='%Y-%m-%d %X',
				filename=Log_FileName,
				filemode='w')


'''打印到屏幕日志'''
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] [line:%(lineno)d] [%(levelname)s]: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
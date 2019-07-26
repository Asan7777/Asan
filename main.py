from commonfun.htmltestrunner.HTMLTestRunner import HTMLTestRunner
from commonfun import sendreport
import time, os, sys, unittest
from commonfun import installinfo
from commonfun.apkinfo import ApkInfo, apk_path
from commonfun.talk import ding_talk
from commonfun.sendreport import sendemail

apk_seat = apk_path()   #获取APK位置
apk_package = ApkInfo(apk_seat).get_apk_pkg()   #获取APK包名

#========================将测试用例添加到测试套件========================
def creatsuite():
	testunit = unittest.TestSuite()
	#testDir = (os.getcwd()+ '/all_script/'+ apk_package + '/')
	#testDir = 'C:\\Users\\170432\\Desktop\\Test_appium\\TestAppium\\Test_case'


	# os.chdir(directory)  # 切换到directory目录
	testDir = (os.getcwd() + '/Test_case')
	# print(testDir)

	#定义discover方法的参数
	discover = unittest.defaultTestLoader.discover(
		testDir,
		pattern = 'test_*.py',
		top_level_dir = None)

	#discover方法筛选出来的用例，循环添加到测试套件中
	for test_case in discover:
		testunit.addTests(test_case)
	return testunit

#创建图片存放文件夹
img_file_name = sendreport.create_img()
#创建测试报告文件夹result
result_path = sendreport.create_result()
#创建测试报告.html
file_name = sendreport.create_html()
#创建log文件
log_file = sendreport.log_result()



fp = open(file_name, 'wb')
runner = HTMLTestRunner(
	stream = fp,
	title = 'APP测试用例报告',
	description = u'APP用例执行情况')

if __name__ == '__main__':

	os.system('start startAppiumServer.bat')   #启动appium服务
	time.sleep(6) #等待appium服务启动完毕
	installinfo.installApk()  #安装apk
	runner.run(creatsuite())
	fp.close()
	ding_talk()   #钉钉推送
	sendreport.sendemail()  #执行完成发送邮件
	os.system('start stopAppiumServer.bat')   #关闭appium服务
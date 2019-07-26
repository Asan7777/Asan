import sys
#模块的和自己的脚本不在一个目录下，在脚本开头加sys.path.append()
sys.path.append("..")
from commonfun import apkoute
from appium import webdriver
from commonfun.apkinfo import ApkInfo,apk_path
newlist = apkoute.apk_route() #获取APK路径
apk_seat = apk_path()   #获取APK位置
apk_package = ApkInfo(apk_seat).get_apk_pkg()#获取APK包名
#apk_activity = ApkInfo(apk_seat).get_apk_activity()#获取apk启动类

def test_phone():
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '5.1'
	desired_caps['noReset'] = True  # 不需要每次都安装apk
	desired_caps['app'] = newlist  # 测试apk包
	desired_caps['deviceName'] = '127.0.0.1:62001'
	desired_caps['unicodeKeyboard'] = 'True'  # 使用unicode输入法
	desired_caps['resetKeyboard'] = 'True'  # 重置输入法到初始状态
	# 如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
	desired_caps['appPackage'] = apk_package
	desired_caps['appActivity'] = 'com.intelligent.reader.activity.SplashActivity'
	desired_caps['noReset'] = 'True'
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	return driver
test_phone()

# test_phone()
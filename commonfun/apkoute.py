import os

#获取APK文件，输入路径
def apk_route():
	local_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	# 获取APP文件夹下的.apk文件
	NEW_LIST = []
	items = os.listdir(local_path + '\\Test_app\\')
	for names in items:
		if names.endswith(".apk"):
			NEW_LIST.append(names)
			file = local_path + '\\Test_app\\' + NEW_LIST[0]
	return file  #输出APK路径

#print(apk_route())
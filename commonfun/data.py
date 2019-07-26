import os, yaml

#按钮参数返回
def data():
	local_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	f = open( local_path + '\\data\\button.yaml', 'rb')
	file = yaml.load(f)
	f.close()
	return file

#自定义参数返回
def parameter():
	local_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	f = open( local_path + '\\data\\parameter.yaml', 'rb')
	file = yaml.load(f)
	f.close()
	return file

# print(data())
# print(parameter())
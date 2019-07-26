import time

#获取当前系统时间
def get_sys_time():
	TIME_FIXED = '%s'%(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
	# print(TIME_FIXED)
	return TIME_FIXED

#获取当前日期
def get_date_time():
	DATA_TIME = '%s'%(time.strftime("%Y%m%d", time.localtime(time.time())))
	# print(DATA_TIME)
	return DATA_TIME
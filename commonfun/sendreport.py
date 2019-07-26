import time, os, smtplib
import mimetypes, zipfile
from commonfun.emailinfo import EmailInfo
import email.mime.multipart, email.mime.text, email.mime.base
from commonfun import systime
from commonfun.apkinfo import ApkInfo, apk_path
from commonfun.phontoinfo import creat_imgfile


apk_seat = apk_path()   #获取APK位置
apk_package = ApkInfo(apk_seat).get_apk_pkg()   #获取APK包名
get_now_time = systime.get_sys_time()   #获取当前系统时间
get_data_time = systime.get_date_time()   #获取当前日期

#创建html报告文件
def create_result():
	result = creat_imgfile(os.getcwd()+ '/all_script/'+ apk_package + '/report/html_result/')
	return result


#创建日志文件
def log_result():
	result = creat_imgfile(os.getcwd()+ '/all_script/'+ apk_package + '/report/log_result/')
	return result


def create_html():
	html_file = (os.getcwd()+ '/all_script/'+ apk_package + '/report/html_result/')+get_now_time + '测试报告详情.html'
	#os.remove(html_file)
	return html_file

#创建图片放置路径
def create_img():
	img_file =  creat_imgfile((os.getcwd()+ '/all_script/'+ apk_package + '/report/screenpicture/') + get_data_time)
	return img_file



'''
# 压缩文件
def zip_file(path, path_new):
	try:
		import zlib
		compression = zipfile.ZIP_DEFLATED
	except:
		compression = zipfile.ZIP_STORED
	start = path.rfind(os.sep) + 1
	filename = path_new + get_data_time + '运行过程截图.zip'  #压缩后的文件名
	z = zipfile.ZipFile(filename,mode = "w",compression = compression)
	try:
		for dirpath,dirs,files in os.walk(path):
			for file in files:
				if file == filename or file == "zip.py":
					continue
				# print(file)
				z_path = os.path.join(dirpath,file)
				z.write(z_path,z_path[start:])
		z.close()
	except:
		if z:
			z.close()


#邮件收发
def send_mail(FILE_NAMEs):

	# 构造MIMEMultipart对象做为根容器
	main_msg = email.mime.multipart.MIMEMultipart()
	now_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

	#设置根容器属性 (阿里邮箱正常使用)
	From = EmailInfo.from_email()
	To = EmailInfo.to_email()
	Email_Subject = EmailInfo.subject()
	Email_host = EmailInfo.mail_host()
	Email_port = EmailInfo.port()
	Email_User_Name = EmailInfo.user_name()
	Email_Password = EmailInfo.password()
	main_msg['From'] = From
	main_msg['To'] = To
	subject = Email_Subject +time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
	main_msg['Subject'] = Email_Subject
    #服务和端口
	server = smtplib.SMTP_SSL(Email_host, Email_port)
    #设置用户名和密码
	server.login(Email_User_Name, Email_Password)


	# 构造MIMEText对象做为邮件显示内容并附加到根容器
	#定义正文
	mail_body = 'HI, ALL:   这是  ' + now_time +  apk_package + '  结束的自动化测试报告，请您查收。具体内容请参见附件。'
	text_msg= email.mime.text.MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #附加到根容器
	main_msg.attach(text_msg)

	for FILE_NAME in FILE_NAMEs:
		# 读入文件内容并格式化
		data = open(FILE_NAME, 'rb')
		ctype,encoding = mimetypes.guess_type(FILE_NAME)
		if ctype is None or encoding is not None:
			ctype = 'application/octet-stream'
		maintype,subtype = ctype.split('/',1)
		file_msg = email.mime.base.MIMEBase(maintype, subtype)
		file_msg.set_payload(data.read())
		data.close()
		email.encoders.encode_base64(file_msg)  #把附件编码

		# 设置附件头
		basename = os.path.basename(FILE_NAME)
		file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
		main_msg.attach(file_msg)

		# 得到格式化后的完整文本
		fullText = main_msg.as_string()

		# 用smtp发送邮件
	# server.sendmail(From, ["@dingyuegroup.cn", "my126sw@126.com"], fullText)  #添加抄送
	server.sendmail(From, To, fullText)  #不添加抄送

#查找测试报告，调用发邮件功能
def sendReport():
	#找到最新html的文件
	NEW_FILES = []
	result_html = ('D:/TestAppium/all_script/'+ apk_package + '/report/html_result/')
	lists  = os.listdir(result_html)
	lists.sort(key = lambda fn: os.path.getmtime(result_html+ '/'+ fn )
		if not os.path.isdir(result_html+ '/'+ fn ) else 0)
	# print(u'最新测试生成的报告:'+ lists[-1])
	new_file = os.path.join(result_html, lists[-1])
	NEW_FILES.append(new_file)

	# #找到最新log的文件
	# result_dir =  ('D:/TestAppium/all_script/'+ apk_package + '/report/log_result/')
	# lists  = os.listdir(result_dir)
	# lists.sort(key = lambda fn: os.path.getmtime(result_dir+ '/'+ fn )
	# 	if not os.path.isdir(result_dir+ '/'+ fn ) else 0)
	# # print(u'最新测试生成的报告:'+ lists[-1])
	# new_file = os.path.join(result_dir, lists[-1])
	# NEW_FILES.append(new_file)

	#找到最新的zip文件
	zip_result_img = ('D:/TestAppium/all_script/'+ apk_package + '/report/screenpicture/' + get_data_time + '/')
	path_new =  ('D:/TestAppium/all_script/'+ apk_package + '/report/screenpicture/')
	zip_file(zip_result_img, path_new)
	result_img = ('D:/TestAppium/all_script/'+ apk_package + '/report/screenpicture/')
	lists  = os.listdir(result_img)
	lists.sort(key = lambda fn: os.path.getmtime(result_img+ '/'+ fn )
		if not os.path.isdir(result_img+ '/'+ fn ) else 0)
	# print(u'最新测试生成的报告:'+ lists[-1])
	new_file = os.path.join(result_img, lists[-1])
	NEW_FILES.append(new_file)

	#print (NEW_FILES)

	#调用发邮件模块
	send_mail(NEW_FILES)
sendReport()
'''



#发送邮件
import smtplib
import email.mime.multipart, email.mime.text, email.mime.base
from email.header import Header
from email.mime.text import MIMEText
from commonfun.emailinfo import EmailInfo
import os

From = EmailInfo.from_email()
To = EmailInfo.to_email()
Email_Subject = EmailInfo.subject()
Email_host = EmailInfo.mail_host()
Email_port = EmailInfo.port()
Email_User_Name = EmailInfo.user_name()
Email_Password = EmailInfo.password()


def sendemail():

    message = MIMEText('邮件内容', 'plain', 'utf-8') # 内容, 格式, 编码
    message['From'] = "{}".format(From)
    message['To'] = ",".join(To)
    #邮件标题
    message['Subject'] = Email_Subject
    try:
        smtpObj = smtplib.SMTP_SSL(Email_host, Email_port)  # 启用SSL发信, 端口一般是465
        smtpObj.login(Email_User_Name, Email_Password)  # 登录验证
        smtpObj.sendmail(From, To, message.as_string())  # 发送
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)



import yaml, os

def get_email_info():
	local_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #获取当前项目的根路径
	f = open( local_path + '\\commonfun\\emailconfig.yaml', 'rb')
	datas = yaml.load(f)
	f.close()
	return datas
#print(get_email_info())

class EmailInfo():
	#静态方法不需要实例化可以直接调用
	@staticmethod
	def from_email():
		From_email = get_email_info()
		return From_email['From_email']


	@staticmethod
	def to_email():
		To_email = get_email_info()
		return To_email['To_email']

	@staticmethod
	def subject():
		Subject = get_email_info()
		return Subject['Subject']

	@staticmethod
	def mail_host():
		Mail_host = get_email_info()
		return Mail_host['Mail_host']

	@staticmethod
	def port():
		Port = get_email_info()
		return Port['Port']

	@staticmethod
	def user_name():
		User_name = get_email_info()
		return User_name['User_name']

	@staticmethod
	def password():
		Password = get_email_info()
		return Password['Password']


#print(EmailInfo.from_email())
#发送邮件
import smtplib
import email.mime.multipart, email.mime.text, email.mime.base
from email.header import Header
from email.mime.text import MIMEText
from get_package.emailinfo import EmailInfo
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

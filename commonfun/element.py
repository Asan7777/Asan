from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commonfun.log import logging

#重写元素定位的方法
class Action(object):
	#初始化
	def __init__(self, se_driver):
		self.driver = se_driver

	#通过resource-id定位
	def find_id(self, id):
		try:
			f = self.driver.find_element_by_id(id)
			logging.info("通过resource-id定位到：%s"%(id))
			return f
		except Exception as e:
			logging.info("%s：通过resource-id未找到"%(id))

	#通过class定位
	def find_class_name(self, name):
		try:
			f = self.driver.find_element_by_class_name(name)
			logging.info("通过class定位到：%s"%(name))
			return f
		except Exception as e:
			logging.info("%s：通过class未找到"%(name))

	#通过text定位
	def find_au(self, name):
		try:
			f = self.driver.find_element_by_android_uiautomator('text(\"' + name +'\")')
			logging.info("通过text定位到：%s"%(name))
			return f
		except Exception as e:
			logging.info("%s：通过text未找到"%(name))

	#通过xpath定位
	def find_xpath(self, xpath):
		try:
			f = self.driver.find_element_by_xpath(xpath)
			logging.info("通过xpath定位到：%s"%(xpath))
			return f
		except Exception as e:
			logging.info("%s：通过xpath未找到"%(xpath))

	#通过content-desc
	def find_ai(self, content_desc):
		try:
			f = self.driver.find_element_by_accessibility_id(content_desc)
			logging.info("通过content_desc定位到：%s"%(content_desc))
			return f
		except Exception as e:
			logging.info("%s：通过content_desc未找到"%(content_desc))

	#调取手机键盘按键
	#调取手机Enter键
	def key_event(self):
		try:
			self.driver.keyevent(66)
			logging.info("调取手机Enter键")
		except Exception as e:
			logging.info("未能输入Enter键")

	#判断toast信息
	def find_toast(self, message):
		'''判断toast信息'''
		try:
			element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
			logging.info("获取toast信息：%s"%(message))
			return element
		except:
			logging.info("%s：toast信息未找到"%(message))
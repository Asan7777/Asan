import xlrd
import xlwt
import os
from xlutils.copy import copy

#获取Excel表格
#获取根路径
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
excel_home = path + '\\ExcelHome\\接口测试.xlsx'
'''

#获取Excel表格
#获取根路径
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
excel_home = path + '\\ExcelHome\\接口测试.xlsx'

def read_excel():

    #print(excel_home)
    #打开Excel
    work_excel = xlrd.open_workbook(excel_home,'r')
    #print (work_excel.sheet_names())
    #获取sheet2
    # sheet2 = work_excel.sheet_names()[1]
    # print(sheet2)
    # sheet2 = work_excel.sheet_by_index(1)
    # print(sheet2)
    #获取sheet2内容
    sheet2 = work_excel.sheet_by_name('Sheet2')
    #获取sheet的名称，行数，列数
    print(sheet2.name,sheet2.nrows,sheet2.ncols)
    s2 = work_excel.sheets()[1]
    print(s2)
    #获取第三行内容
    rows = sheet2.row_values(3)
    #获取第四行内容
    cols = sheet2.col_values(6)
    print("第三行的内容是%s"%rows,"第四列的内容是%s"%cols)
    #获取单元格内容
    ID = sheet2.cell(1,6)
    print(ID)
    URL = sheet2.cell_value(2,0)
    print(URL)
    RESQUTE = sheet2.row(1)[2]
    print(RESQUTE)
    #获取单元格内容的数据类型
    print(sheet2.cell(1,2).ctype)
    print(sheet2.cell(4,5))






# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：excel的封装

workbook = None
def open_excel(path,sheetName):
    """打开excel"""
    global workbook
    if (workbook == None):
        workbook = xlrd.open_workbook(path, on_demand=True)
def get_sheet(sheetName):
    """获取页名"""
    global workbook
    return workbook.sheet_by_name(sheetName)
def get_rows(sheet):
    """获取行号"""
    return sheet.nrows
def get_content(sheet, row, col):
    """获取表格中内容"""
    return sheet.cell(row, col).value
def release(path):
    """释放excel减少内存"""
    global workbook
    workbook.release_resources()
    del workbook
open_excel(excel_home,'sheet2')

'''


class OperationExcel:
	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id
		else:
			self.file_name = excel_home
			self.sheet_id = 1
		self.data = self.get_data()
	#获取sheets的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables
	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows
	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

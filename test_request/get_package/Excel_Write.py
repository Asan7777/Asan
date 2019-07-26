import xlrd,xlwt
import os
def set_style(name,height,bold=False):
    #初始化表格样式
    style = xlwt.XFStyle()
    #为样式创建字体
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders

    return style
# write_merge(x, x + m, y, w + n, string, sytle)
# x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，style表示单元格样式。其中，x，y，w，h，都是以0开始计算的
#写excel
def write_excel():
    f = xlwt.Workbook()
    #创建第一个sheet
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    #定义行
    row0 = [u'ID',u'URL',u'请求类型',u'data',u'预期结果']
    #定义列
    col0 = [u'1',u'2',u'3',u'4']
    #print(len(col0))
# write_excel()
    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    #生成第一列
    i,j = 1,0
    while j<len(col0) or i < 20:
        sheet1.write(i,0,i,set_style('Arial',220,True))
        i += 1
        j += 1
    #指定单元格写入内容
    sheet1.write(1,1,'www.baidu.com')
    sheet1.write(1,2,'get')
    sheet1.write(1,3,'data')
    sheet1.write(1,4,'data')
    #将超链接写入单元格
    n = "HYPERLINK"
    sheet1.write(1,5,xlwt.Formula(n +'("http://www.cnblogs.com/zhoujie";"jzhou\'s blog")'))
    #获取写入表格路径
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    excel_home = path + '\\ExcelHome\\test_write.xls'
    #保存到表格
    f.save(excel_home)

    #创建第二个sheet2
    #sheet2 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)


#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
@author:hjy
@project:s14day20
@file:test.py
@time:2020/5/19   13:58
'''

import xlrd
def strs(row):
    values = ""
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i])
    return values
# 打开文件
data = xlrd.open_workbook("D:/python/demo/数据库文件转成excel文件/output.xlsx")
sqlfile = open("learn.txt", "a")  # 文件读写方式是追加
table = data.sheets()[0]  # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(1)  # 某一行数据
# 打印出行数列数
for ronum in range(1, nrows):     #控制显示第几行，即去除行标题之类的
        row = table.cell_value(rowx=ronum, colx = 2) #只需要修改你要读取的列数-1
        row = str(row)
        values = strs(row)  # 调用函数，将行数据拼接成字符串
        sqlfile.writelines(values + "\n")  # 将字符串写入新文件
        # sqlfile.writelines(values + "\t")  # 将字符串写入新文件

sqlfile.close()  # 关闭写入的文件

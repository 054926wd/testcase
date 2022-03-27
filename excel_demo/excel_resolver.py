# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 22:27
# @Author  : 多情的小怪兽
# @File    : excel_resolver.py
import openpyxl
from web_demo.web_element import WebDemo


# 打开excel文件
excel = openpyxl.load_workbook('../excel_demo/excel_data.xlsx')
# 读取sheet名称
sheets = excel.sheetnames
for sheet1 in sheets:
    sheet = excel[sheet1]
    for values in sheet.values:
        params = {}
        params["name"] = values[2]
        params["value"] = values[3]
        params["txt"] = values[4]
        # name = values[2]
        # value = values[3]
        # txt = values[4]
        if type(values[0]) is int:
            print(values)
            if values[1] == "browser":
                wd = WebDemo(params['txt'])
            else:
                getattr(wd,values[1])(**params)
        else:
            pass

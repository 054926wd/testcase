# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 22:27
# @Author  : 多情的小怪兽
# @File    : excel_resolver.py
import openpyxl
from web_demo.web_element import WebDemo
from loguru import logger

logger.add('../target/{time:YYYYMMDD}/{time:YYYY-MM-DD_HH-mm-ss}.log',format="{time:YYYY-MM-DD HH:mm:ss} {name} {file} {level} {message}",level="INFO",retention="10 days",encoding='utf-8')

# 打开excel文件
excel = openpyxl.load_workbook('../excel_demo/excel_data.xlsx')
# 读取sheet名称
sheets = excel.sheetnames
for sheet1 in sheets:
    sheet = excel[sheet1]
    logger.info("------------正在执行{}的测试用例------------".format(sheet1))
    # print("----------{}----------".format(sheet1))
    for values in sheet.values:
        params = {}
        params["name"] = values[2]
        params["value"] = values[3]
        params["txt"] = values[4]
        # name = values[2]
        # value = values[3]
        # txt = values[4]
        try:
            if type(values[0]) is int:
                if values[1] == "browser":
                    wd = WebDemo(params['txt'])
                else:
                    getattr(wd,values[1])(**params)
                logger.info("正在执行:第{}步-----执行内容为:{}-{}".format(values[0],values[5],values[4]))
                # print("正在执行:{}-----执行内容为:{}".format(values[5],values[4]))
        except Exception as error:
            logger.error("第{}步执行错误：{}".format(values[0],error))
    logger.info("------------执行{}测试用例成功------------".format(sheet1))
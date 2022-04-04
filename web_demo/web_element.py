# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 22:32
# @Author  : 多情的小怪兽
# @File    : web_element.py

import os
from time import sleep
from loguru import logger
from datetime import datetime
from selenium import webdriver

def browser(type_):
    try:
        driver = getattr(webdriver,type_)()
    except:
        logger.warning("出现异常,启动默认浏览器Chrome")
        driver = webdriver.Chrome()
    return driver

class WebDemo:
    def __init__(self,type_):
        self.driver = browser(type_)
        # self.driver = webdriver.Chrome()

    #最大化浏览器
    def max_web(self,**kwargs):
        self.driver.maximize_window()

    # 打开浏览器
    def open(self, **kwargs):
        # self.driver.get("http://www.baidu.com")
        self.driver.get(kwargs['txt'])

    # 元素定位
    def locator(self,name,value):
        return self.driver.find_element(name,value)
        # self.driver.find_element('ID','kw').send_keys('123456')

    # 元素输入
    def input(self, **kwargs):
        self.locator(kwargs['name'],kwargs['value']).send_keys(kwargs["txt"])

    # 元素点击
    def click(self, **kwargs):
        self.locator(kwargs['name'],kwargs['value']).click()

    #切换至新打开的标签页
    def table(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    #屏幕截图
    def screenshot(self,filename='屏幕截图',**kwargs):
        screenshot_dir = '../picture'  # 当前目录下的screenshot文件夹；或设置其他目录
        if not os.path.exists(screenshot_dir):  # 不存在则创建该目录
            os.mkdir(screenshot_dir)

        nowdate = datetime.now().strftime('%Y%m%d')  # 当日日期
        screenshot_today_dir = os.path.join(screenshot_dir, nowdate)  # 当前日期文件夹
        if not os.path.exists(screenshot_today_dir):
            os.mkdir(screenshot_today_dir)  # 不存在则创建

        nowtime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # 时间戳
        filename = nowtime + filename + ".png"  # 拼接文件名 时间戳+文件名+.png
        filepath = os.path.join(screenshot_today_dir, filename)
        try:
            self.driver.get_screenshot_as_file(filepath) # 截图，文件名=filename+时间戳
            logger.info("截图成功-----{}".format(filepath))
        except Exception as error:
            logger.error("截图失败")


    # 退出浏览器
    def quit(self,**kwargs):
        self.driver.quit()

    # 强制等待
    def wait(self, **kwargs):
        sleep(kwargs['txt'])

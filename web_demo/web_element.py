# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/3/24 22:32
# @Author  : 多情的小怪兽
# @File    : web_element.py
from selenium import webdriver
from time import sleep

#
def browser(type_):
    try:
        driver = getattr(webdriver,type_)()
    except:
        print("出现异常启动默认浏览器Chrome")
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

    # 退出浏览器
    def quit(self,**kwargs):
        self.driver.quit()

    # 强制等待
    def wait(self, **kwargs):
        sleep(kwargs['txt'])

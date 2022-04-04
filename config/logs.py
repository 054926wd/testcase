# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/4 12:52
# @Author  : 多情的小怪兽
# @File    : logs.py
from loguru import logger

class Config:
    def loggs(self):
        logger.add('./target/{time}.log',format="{name} {level} {message}",level="INFO",rotation='50 MB',encoding='utf-8')


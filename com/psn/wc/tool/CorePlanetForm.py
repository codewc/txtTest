#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = '王春'

import  ConfigParser
import  logging

"""
def getlogger():
    logger = logging.getLogger('G'):
    return logger;
def get_config():
        config = ConfigParser.ConfigParser()
        with open("mycfg.cfg") as cfg:
            config.readfp(cfg)
            path = config.get("info","path")
            savepath = config.get("info","save_path")
        print("初始化完成")
        return config
"""
config = None
class ConfigUser():
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        with open("mycfg.cfg") as cfg:
            config = self.config
            config.readfp(cfg)
            path = config.get("info","path")
            print(path)

config = ConfigUser().config
print(config)
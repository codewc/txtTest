#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = '王春'

import  ConfigParser
class TxtTools(object):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        with open("mycfg.cfg") as cfg:
            config.readfp(cfg)
            self.path = config.get("info","path")
            self.savepath = config.get("info","save_path")
            print(self.savepath)
        self.index = 0
        self.mesage = "no message!!"
        print("初始化完成")
    def readBook(self):
        self.savef = open(self.savepath,"w")
        try:
            f = open(self.path,"r")
            s = f.readlines()
            for k in s:
                pass
        except:
            print("出错了")
        finally:
            f.close()
            self.savef.close()

c = TxtTools()
print(c.index)
print(c.path)
c.readBook()
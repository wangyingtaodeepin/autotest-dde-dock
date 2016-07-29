#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class dockClass(object):
    def __init__(self):
        self.displaymode_fashion   = 0    # 时尚
        self.displaymode_efficient = 1    # 高效

        self.hidemode_keepshowing = 0    # 一直显示
        self.hidemode_keephidden  = 1    # 一直隐藏
        self.hidemode_smarthide   = 2    # 只能隐藏

        self.position_top    = 0    # 顶部
        self.position_right  = 1    # 右侧
        self.position_botton = 2    # 底部，默认值
        self.position_left   = 3    # 左侧

        self.hidestate_show  = 1    # 显示
        self.hidestate_hide  = 2    # 隐藏

dock = dockClass()

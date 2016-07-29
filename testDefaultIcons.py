#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils

class FashionDefaultIcons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaultfashioniconlist = ["Launcher",
                               "显示桌面",
                               "多任务视图",
                               "文件",
                               "深度商店",
                               "深度音乐",
                               "Google Chrome",
                               "控制中心",
                               "system-tray-fashion-mode-item",
                               "shutdown-shutdown",
                               "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultmode = utils.getDdeDockDisplayMode()

    @classmethod
    def tearDownClass(cls):
        pass
    
    def testExists(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % name)

    def testDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)

    def testExistsChangedMode(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FashionDefaultIcons('testExists'))
    suite.addTest(FashionDefaultIcons('testDifferentMode'))
    suite.addTest(FashionDefaultIcons('testExistsChangedMode'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())

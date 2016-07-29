#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils

class EfficientDefaultIcons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaultefficienticonlist = ["Launcher",
                                        "显示桌面",
                                        "多任务视图",
                                        "文件",
                                        "深度商店",
                                        "深度音乐",
                                        "Google Chrome",
                                        "控制中心",
                                        "shutdown-shutdown",
                                        "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)

    def testExists(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % name)

    def testDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)

    def testExistsChangedMode(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(EfficientDefaultIcons('testExists'))
    suite.addTest(EfficientDefaultIcons('testDifferentMode'))
    suite.addTest(EfficientDefaultIcons('testExistsChangedMode'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils

class testDefaultIcons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaulticonlist = ["Launcher",
                               "显示桌面",
                               "文件",
                               "深度商店",
                               "深度音乐",
                               "Google Chrome",
                               "控制中心",
                               "shutdown",
                               "datetime"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultmode = utils.getDdeDockMode()

    @classmethod
    def tearDownClass(cls):
        pass
    
    def testExists(self):
        for name in self.defaulticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region" % name)

    def testDifferentMode(self):
        mode = utils.getDdeDockMode()
        self.assertTrue(0 == utils.dock.fashionmode)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(testDefaultIcons('testExists'))
    suite.addTest(testDefaultIcons('testDifferentMode'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())

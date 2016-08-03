#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from lib import runner

result = True

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class FashionFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.casename = "all-2471:时尚模式功能测试"
        cls.ddedockobject = utils.getDdeDockObject()
        cls.dock_mainwindow = "dock-mainwindow"

    @classmethod
    def tearDownClass(cls):
        global result
        if result == True:
            print("Successful")

        if result == False:
            print("Failed")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBasicFunction(self):
        defaultdisplaymode = utils.getDdeDockDisplayMode()
        self.assertTrue(utils.dock.displaymode_fashion == defaultdisplaymode)
        defaultposition = utils.getDdeDockPosition()
        self.assertTrue(utils.dock.position_bottom == defaultposition)
        defaulthidestate = utils.getDdeDockHideState()
        self.assertTrue(utils.dock.hidestate_show == defaulthidestate)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(width > 0)
        self.assertTrue(height > 0)

    def testChangeDisplayMode(self):
        self.assertTrue(True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FashionFunction('testBasicFunction'))
    suite.addTest(FashionFunction('testChangeDisplayMode'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())

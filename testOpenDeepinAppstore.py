#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils

class DeepinAppstore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.icon_deepinappstore = "深度商店"
        cls.window_name = "深度商店 — Deepin Store"
        cls.ddedockobject = utils.getDdeDockObject()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOpen(self):
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        iconobj.click()
        sleep(4)
        win = utils.findWindow(self.window_name)
        self.assertTrue(win)

    def testClose(self):
        win = utils.findWindow(self.window_name)
        utils.closeWindow(win)
        win = None
        sleep(3)
        win = utils.findWindow(self.window_name)
        self.assertFalse(win)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DeepinAppstore('testOpen'))
    suite.addTest(DeepinAppstore('testClose'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils

class FashionIconsPopup(unittest.TestCase):
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
                               "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition    = utils.getDdeDockPosition()

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)
    
    def testPopupExists(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "system-tray-fashion-mode-item" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
                sleep(3)
            elif name == "system-tray-fashion-mode-item":
                icon.click()
                icon_popup = self.ddedockobject.child('sys-tray-popup')
                sleep(3)
                icon.click()
                sleep(3)
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
                sleep(3)
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup") 
                sleep(3)

            self.assertTrue(icon_popup, "Position bottom: Can't find the [ %s ] icon-popup in the dock region with Fashion Mode" % name)
            print("find the popup window with icon: %s" % name)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FashionIconsPopup('testPopupExists'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from time import sleep
from lib import utils

class EfficientIconsPopup(unittest.TestCase):
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
                                        "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition    = utils.getDdeDockPosition()

        if utils.dock.displaymode_efficient != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)

    def testPopupExists(self):
        for name in self.defaultefficienticonlist:
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
    suite.addTest(EfficientIconsPopup('testPopupExists'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())

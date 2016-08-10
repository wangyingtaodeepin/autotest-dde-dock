#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionDefaultIcons
import testEfficientDefaultIcons
import testFashionIconsPopup
import testEfficientIconsPopup
import testFashionFunction
import testEfficientFunction
import testFashionExistLeft
import testFashionExistRight
import testFashionDockSize
import testEfficientDockSize
import testOtherDirectionDockSize
import testDockKeepShown
import testDockKeepHidden

def main():
    suite00 = testFashionDefaultIcons.suite()
    suite01 = testEfficientDefaultIcons.suite()
    suite02 = testFashionIconsPopup.suite()
    suite03 = testEfficientIconsPopup.suite()
    suite1 = testFashionFunction.suite()
    suite2 = testEfficientFunction.suite()
    suite3 = testFashionExistLeft.suite()
    suite4 = testFashionExistRight.suite()
    suite5 = testFashionDockSize.suite()
    suite6 = testEfficientDockSize.suite()
    suite7 = testOtherDirectionDockSize.suite()
    suite8 = testDockKeepShown.suite()
    suite9 = testDockKeepHidden.suite()

    alltests = unittest.TestSuite((suite00, suite01, suite02, suite03,
                                   suite1, suite2, suite3, suite4,
                                   suite5, suite6, suite7, suite8,
                                   suite9))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()

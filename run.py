#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionDefaultIcons
import testEfficientDefaultIcons
import testFashionIconsPopup
import testEfficientIconsPopup
import testOpenDeepinAppstore
import testIconDock

def main():
    suite1 = testFashionDefaultIcons.suite()
    suite2 = testEfficientDefaultIcons.suite()
    suite3 = testFashionIconsPopup.suite()
    suite4 = testEfficientIconsPopup.suite()
    suite5 = testOpenDeepinAppstore.suite()
    suite6 = testIconDock.suite()

    alltests = unittest.TestSuite((suite1, suite2, suite3, suite4,
                                   suite5, suite6))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()

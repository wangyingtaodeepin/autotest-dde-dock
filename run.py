#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionDefaultIcons
import testEfficientDefaultIcons
import testFashionIconsPopup
import testEfficientIconsPopup

def main():
    suite1 = testFashionDefaultIcons.suite()
    suite2 = testEfficientDefaultIcons.suite()
    suite3 = testFashionIconsPopup.suite()
    suite4 = testEfficientIconsPopup.suite()

    alltests = unittest.TestSuite((suite1, suite2, suite3, suite4))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()
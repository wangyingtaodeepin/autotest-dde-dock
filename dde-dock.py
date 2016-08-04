#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionFunction
import testEfficientFunction
import testFashionExistLeft
import testFashionExistRight

def main():
    suite1 = testFashionFunction.suite()
    suite2 = testEfficientFunction.suite()
    suite3 = testFashionExistLeft.suite()
    suite4 = testFashionExistRight.suite()

    alltests = unittest.TestSuite((suite1, suite2, suite3, suite4))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()

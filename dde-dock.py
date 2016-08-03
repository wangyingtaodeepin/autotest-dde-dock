#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionFunction
import testEfficientFunction

def main():
    suite1 = testFashionFunction.suite()
    suite2 = testEfficientFunction.suite()

    alltests = unittest.TestSuite((suite1, suite2))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()

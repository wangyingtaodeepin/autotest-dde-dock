#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionDefaultIcons
import testEfficientDefaultIcons

def main():
    suite1 = testFashionDefaultIcons.suite()
    suite2 = testEfficientDefaultIcons.suite()

    alltests = unittest.TestSuite((suite1, suite2))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()

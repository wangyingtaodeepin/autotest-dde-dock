#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import testFashionFunction

def main():
    suite1 = testFashionFunction.suite()

    alltests = unittest.TestSuite((suite1,))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()

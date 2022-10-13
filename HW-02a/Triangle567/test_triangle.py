# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInputTooBig(self):
        self.assertEqual(classify_triangle(1,1,201),'InvalidInput')
    
    def testInvalidInputBelowZero(self):
        self.assertEqual(classify_triangle(0,1,2),'InvalidInput')
    
    def testInvalidInputNotAnInteger(self):
        self.assertEqual(classify_triangle(3,4,"apple"),'InvalidInput')

    def testIsocelesTriangle(self):
        self.assertEqual(classify_triangle(2,2,3),'Isoceles')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(4,5,10),'NotATriangle')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(6,7,8),'Scalene')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


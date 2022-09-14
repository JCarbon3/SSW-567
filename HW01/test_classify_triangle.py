import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):
    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(4,4,4),"Equilateral")
        self.assertEqual(classify_triangle(3,4,5),"Right")
        self.assertEqual(classify_triangle(4,4,5),"Isosceles")
        self.assertEqual(classify_triangle(4,5,6),"Scalene")
        self.assertEqual(classify_triangle(0,4,4),"A triangle must have 3 sides of non-zero length.")
        self.assertEqual(classify_triangle(4,4,4),"Equilateral")

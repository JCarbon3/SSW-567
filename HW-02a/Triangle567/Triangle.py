# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(side_1,side_2,side_3):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.\

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not isinstance(side_1,int) or not isinstance(side_2,int) or not isinstance(side_3,int):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if side_1 > 200 or side_2 > 200 or side_3 > 200:
        return 'InvalidInput'

    if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
        return 'InvalidInput'


    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_1 >= (side_2 + side_3)) or (side_2 >= (side_1 + side_3)) or (side_3 >= (side_1 + side_2)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_1 == side_2 and side_2 == side_3:
        return 'Equilateral'
    if (((side_1 ** 2) + (side_2 ** 2)) == (side_3 ** 2)) or (((side_1 ** 2) + (side_3 ** 2)) == (side_2 ** 2)) or (((side_2 ** 2) + (side_3 ** 2)) == (side_1 ** 2)):
        return 'Right'
    if (side_1 != side_2) and  (side_2 != side_3) and (side_1 != side_3):
        return 'Scalene'
    return 'Isoceles'

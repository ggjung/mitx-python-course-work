# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:19:48 2017

@author: g

Week 2 Problem Set 2 Problem 1
Regular polygon: Sum of area and perimeter^2 

Given the number of sides and length of each side, find the area, perimeter, 
and the sum of area + perimeter^2.

Polygon must have more than 2 sides.

Uses math library

"""

def checkPoly(n,s):
    """
    Input
        n: number of sides, integer
        s: length of each side, integer
        
    Output
        True if valid number of sides, False otherwise
    """
    if n>2:
        return True
    else:
        return False

def polyArea(n,s):
    """
    Input
        n: number of sides, integer
        s: length of each side, integer
        
    Output
        area of polygon, float
    """
    import math
    return (0.25 * n * s * s)/math.tan(math.pi/n)

def polyPerim(n,s):
    """
    Input
        n: number of sides, integer
        s: length of each side, integer
        
    Output
        perimeter of polygon, float
    """
    return n*s

def polysum(n,s):
    """
    Input
        n: number of sides, integer
        s: length of each side, integer
        
    Output
        sum of area + perimeter^2, float rounded to 4 decimal places
    """
    if checkPoly(n,s):
        result = polyArea(n,s) + polyPerim(n,s)**2
        return round(result,4)
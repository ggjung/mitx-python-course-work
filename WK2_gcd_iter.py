# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:32:28 2017

@author: g

Finds the greatest common denominator of 2 integers iteratively.
"""
def gcdIter(a,b):
    
    if a>b: 
        smaller = b
        larger = a
    else:
        smaller = a
        larger = b
        
    guess = smaller
    
    for i in range(smaller, 0, -1):
        if larger%guess == 0:
            if smaller%guess == 0:
                break
        guess -= 1
        
    return guess
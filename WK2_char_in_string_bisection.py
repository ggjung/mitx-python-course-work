# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:55:59 2017

@author: g

Determines if a character is in a string using bisection search.
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        result = (char == aStr)

#   tests depending on length of string being even/odd    
    else: 
        testChar = aStr[int(len(aStr)/2)]
        if len(aStr)%2 == 0:
            if char < testChar:
                result = isIn(char, aStr[:int(len(aStr)/2)])
            elif char > testChar:
                result = isIn(char, aStr[int(len(aStr)/2):])
            else:
                result = isIn(char, aStr[int(len(aStr)/2)])
        else:
            if char < testChar:
                result = isIn(char, aStr[:int(len(aStr)/2)])
            elif char > testChar:
                result = isIn(char, aStr[int(len(aStr)/2)+1:])
            else:
                result = isIn(char, aStr[int(len(aStr)/2)])

    return result
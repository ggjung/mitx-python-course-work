# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:30:31 2017

@author: g

Week 1 Problem set 1 Problem 2
Bob Counter

Given a lowercase string input, it will count the number of 'bob's in the input and print the result.
Not a particularly clever solution.
"""

numBobs = 0

s = input("Enter any lowercase string: ")

for letter in range(0,len(s)-2,1):
    if s[letter] == "b":
        if s[letter+1] == "o":
            if s[letter+2] == "b":
                numBobs += 1
        
print("Number of bobs: " + str(numBobs))
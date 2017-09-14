# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:15:39 2017

@author: g

Week 1 Problem set 1 Problem 1
Vowel Counter

Given a lowercase string input, it will count the number of vowels in the input and print the result.
Self expl.
"""

numVowels = 0

s = input("Enter any lowercase string: ")

for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        numVowels += 1
        
print("Number of vowels: " + str(numVowels))
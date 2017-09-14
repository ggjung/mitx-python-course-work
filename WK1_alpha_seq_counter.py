# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:42:29 2017

@author: g

Week 1 Problem set 1 Problem 3
Longest Alphabetical Sequence Finder

Given a lowercase string input, it will find the longest substring in alphabetical order and print the result.

Converts the string into an array of ints (ASCII) but later found out this is not necessary.
For a given letter in the sequence, it will find if the next letter is "the same or larger."
Continues to do this until the next letter is "smaller."
Then compares the current sequence length to current longest sequence.
If current substring is longer, then store the position of its last letter.
Continues to go through each letter until the number of letters left is shorter than the current longest sequence.
Prints result.

"""


arr = []
longestSeq = 1
currentLetter = 0

s = input("Enter any lowercase string: ")

for i in range(0,len(s)):
    arr.append(ord(s[i]))

while (len(s) - currentLetter - longestSeq > 0):
    currentSeq = 1    
    while (len(s) - currentLetter > 1): 
        diff = arr[currentLetter + 1] - arr[currentLetter]
        if diff >= 0:
            currentSeq += 1            
            currentLetter +=1
        else: 
            currentLetter +=1
            break
        if currentSeq > longestSeq:
                longestSeq = currentSeq   
                lastLetter = currentLetter

if longestSeq == 1:
    print("Longest substring in alphabetical order is: " + s[0])
else:
    print("Longest substring in alphabetical order is: " + s[lastLetter-longestSeq+1:lastLetter+1])
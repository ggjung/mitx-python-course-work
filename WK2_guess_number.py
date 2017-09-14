# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:15:55 2017

@author: g

Week 2 Coding Exercise
Guess my number

Guesses the user's number using binomial search.
Self expl.
"""

# initializations...
high = 100
low = 0
ans = int((high + low)/2)
response = ""

print("Please think of a number between 0 and 100!")

while response != "c":
    
    print("Is your secret number " + str(ans) + "?")
    
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if response == "h":
        if ans == 1:
            ans = 0
            break
        high = ans
        ans = int((high + low)/2)
    
    elif response == "l":
        if ans == 99:
            ans = 100
            break
        low = ans
        ans = int((high + low)/2)
        
    elif response == "c":
        break
    
    else:
        print("Sorry, I did not understand your input.")
        
print("Game over. Your secret number was: " + str(ans))

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:11:44 2017

@author: g

Week 2 Problem set 2 Problem 3
Paying off debt in a year with fixed payment

Given predefined values for balance, annual interest rate
calculates the fixed payment needed to pay off the debt at the end of 1 year.

Uses bisection method to search
Lower bound: Balance / 12
Upper bound: Balance with interest after 12 months
"""

balance = 999999
annualInterestRate = 0.18

def balanceCalc(balance, apr, payment):
    """
    Input
        balance: balance at the time, int or float
        apr: annual interest rate, float
        payment: monthly payment (given as % of balance), float
        
    Output
        balance after payment and interest, float
    """
    balance = balance - payment
    balance = balance*(1+apr/12)
    return balance

def yearEndBalance(balance, monthlyPayment):
    """
    Input
        balance: balance at the time, int or float
        monthlyPayment: monthly payment (given as % of balance), float
        
    Output
        balance after payment and interest in 12 months, float
    """
    for i in range(12):
        balance = balanceCalc(balance, annualInterestRate, monthlyPayment)
    return balance
    
def debtCheck(balance, lower, upper):
    """
    Input
        balance: balance at the time, int or float
        lower: lower bound of bisection search for lowest payment, int or float
        upper: upper bound of bisection search for lowest payment, int or float
        
    Output
        minimum payment needed to pay off balance in 12 months
    """
    guess = (upper + lower) / 2
    
    if abs(yearEndBalance(balance, guess)) < .01:
        return guess
    
    else:
        if yearEndBalance(balance, guess) > 0: 
            return debtCheck(balance, guess, upper)
        else: 
            return debtCheck(balance, lower, guess)

#this outputs the minimum payment, rounded to 2 decimal places
print("Minimum payment: " + str(round(debtCheck(balance, balance/12, (balance * (1 + (annualInterestRate/12))**12) / 12),2)))
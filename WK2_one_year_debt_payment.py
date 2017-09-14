# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:30:55 2017

@author: g

Week 2 Problem set 2 Problem 1
Paying off debt in a year

Given predefined values for balance, annual interest rate, and monthly payment rate
calculates the remaining balance at the end of 1 year.
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def balanceCalc(balance, apr, payment):
    """
    Input
        balance: balance at the time, int
        apr: annual interest rate, float
        payment: monthly payment (given as % of balance), float
        
    Output
        balance after payment and interest, float
    """
    balance = balance*(1-payment)
    balance = balance*(1+apr/12)
    return balance

for i in range(12):
    balance = balanceCalc(balance, annualInterestRate, monthlyPaymentRate)
    
print("Remaining balance: " + str(round(balance,2)))
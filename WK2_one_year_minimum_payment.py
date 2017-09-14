# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:49:31 2017

@author: g

Week 2 Problem set 2 Problem 2
Paying off debt in a year with fixed payment

Given predefined values for balance, annual interest rate
calculates the fixed payment needed to pay off the debt at the end of 1 year.

The fixed payment value will be a multiple of 10.
"""

balance = 3926
annualInterestRate = 0.2

def balanceCalc(balance, apr, payment):
    """
    Input
        balance: balance at the time, int or float
        apr: annual interest rate, float
        payment: monthly payment, int
        
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
        monthlyPayment: monthly payment, int
        
    Output
        balance after payment and interest in 12 months, float
    """
    for i in range(12):
        balance = balanceCalc(balance, annualInterestRate, monthlyPayment)
    return balance
    
def debtCheck(balance, monthlyPayment):
    """
    Input
        balance: balance at the time, int or float
        monthlyPayment: monthly payment, int
        
    Output
        returns minimum monthly payment required to pay off balance in 12 months, rounded to nearest 10
    """
    if yearEndBalance(balance, monthlyPayment) <= 0:
        return monthlyPayment
    else:
        return debtCheck(balance, monthlyPayment + 10)

print("Minimum payment: " + str(debtCheck(balance,0)))
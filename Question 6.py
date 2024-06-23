# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:19:54 2021

@author: Fogol

Project Euler Problem 6
The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is, 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def SumSquares(x):
    y = 0
    if x == 1:
        return 1
    else:
        y = SumSquares(x-1)+(x**2)
        return y

def MultSquares(x):
    y = 0
    while x > 0:
        y = y + x
        x = x - 1
    return y**2
 
def difference(x):
    y = MultSquares(x)-SumSquares(x)
    return y

print(SumSquares(100))
print(MultSquares(100))
print(difference(100))
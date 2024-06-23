# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:28:31 2021

@author: Fogol

Project Euler Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
Num = 999*999

def reverse(x):
    Reverse = 0
    while x >0:
        Remainder = x%10
        Reverse = Reverse*10 + Remainder
        x = x//10
    return Reverse

Stop = False

while (Num > 1) & (Stop != True):
    
    i = 999
    if (reverse(Num) == Num):
        while (i >= 990) & (Stop != True):
            if (Num // i <= 999) & (Num % i == 0):
                print(Num)
                Stop = True
                break
            else:
                i=i-1
        Num = Num -1
        
    else:
        Num = Num-1
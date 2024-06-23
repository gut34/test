# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:02:34 2021

@author: Fogol

Project Euler Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
Max = 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
print(Max)
Num = 2520

while Num < Max:
    if (Num % 20 == 0)&(Num % 19 == 0)&(Num % 18 == 0)&(Num % 17 == 0)&(Num % 16 == 0)&(Num % 14 == 0)&(Num % 13 == 0)&(Num % 11 == 0):
        print(Num)
        break
    else:
        Num = Num + 2

print(Num)
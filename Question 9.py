# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:53:30 2021

@author: Fogol

Project Euler Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
count = 1
C_array = []
Statement = False

for C in range(100,1000):
    if Statement == False:
        for B in range (2,int(C)):
            if Statement == False:
                for A in range (1,int(B)):
                    if Statement == False:
                        if (A**2 + B**2 == C**2) & (A + B + C == 1000):
                            Product = A*B*C
                            print(Product)
                            print(A)
                            print(B)
                            print(C)
                            Statement = True
                            break
    else:
        break
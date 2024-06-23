# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:37:22 2021

@author: Fogol

Project Euler Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def isprime(x):
    for i in range(2,x**0.5 + 1):
        if x % i == 0:
            return False
    return True

count = 2 #isprime does not work for 2, and 3
start = 5
while count < 10001:
    if isprime(start) == True:
        count = count + 1
        start = start + 2
    else:
        start = start + 2

print(start-2)

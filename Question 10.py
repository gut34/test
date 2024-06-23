# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:05:21 2021

@author: Fogol

Project Euler Problem 9
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def isprime(x):
    for i in range(2,int((x/2)+2)):
        if x % i == 0:
            return False
    return True

i = 3
count = 2
while i < 2000000:
    if isprime(i) ==  True:
        count = count + i
        i = i + 2
    else:
        i = i + 2
print(count)
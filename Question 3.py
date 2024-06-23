"""
Created on Tue Jul 27 13:43:17 2021

@author: Fogol

Project Euler Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""   
 
def isprime(x):
    for i in range(2,x-1):
        if x % i == 0:
            return False
    return True


x = 600851475143
y = 1


for i in range (3,int(x/2)):
 
    if (x % i == 0) and isprime(i):
        
        y = i
        print(y)
    
    else:
        
        i = i + 2
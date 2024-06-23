# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:16:23 2021

@author: Fogol
"""

x ='backwards'

def reverse(x):  
    if len(x) == 0:
        return x
    else:
        print(x[len(x)-1])
        x = x[0:len(x)-1:1]
        return reverse(x)

print(reverse(x))
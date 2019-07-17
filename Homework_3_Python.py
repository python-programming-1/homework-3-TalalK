#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:40:48 2019

@author: tkhodr
"""

print("Welcome to Collatz!")

def collatz(num):
    if num % 2 == 0 and num != 1:   # Checks for an even number and if it is 1
        x = num // 2
    elif num % 2 == 1:              # Checks for the odd number
        x = (3*num) +1
    while x == 1:
        print(x)
        break
    while x != 1:          
        print(x)
        num = x         
        return collatz(num)    
print('Please enter an integer ONLY')# Integer inut is requsted here.         
try:
    num = int(input())#Will only accept integers due to the int() FUN
    collatz(num)
except ValueError:
    print('{num}Please only enter ingteger values onto the prompt.')
# I was trying to add a function interpolation
# To give back the given response to the user and ask for an integer.

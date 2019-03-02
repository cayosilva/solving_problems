#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:49:46 2019

@author: void
"""

def revert_number(n):
    reverse = 0
    while n>0:
        last_digit = n % 10
        reverse = (reverse * 10) + last_digit
        n = n // 10
    return reverse

n = int(input()) 
inputs = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    inputs.append(row)

#revert a string may be: print(str(inputs[0][0])[::-1])
for i in range(n):
    result = revert_number(inputs[i][0]) + revert_number(inputs[i][1])
    print (revert_number(result))

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:58:12 2018

@author: aksha
"""


n = int(input("Enter the line from where you want to read : "))
n = n-1
file = "sam.txt"
with open(file,'r') as f :
    a = f.readlines()

    while n<len(a) :
        print(a[n])
        n=n+1

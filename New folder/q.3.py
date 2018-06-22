# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:31:39 2018

@author: aksha
"""

n = int(input("Enter number of elements to be inputed : "))
a = [0]*n
b = [0]*n

i=0
while i < n:
    a[i] = int(input("Enter elements : "))
    i+=1

j=0
while j < n:
    b[j] = a[j] * a[j]
    j+=1

print("Squares of elemnts is :")
k=0
while k < n:
    print(str(b[k]))
    k+=1
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:35:03 2018

@author: aksha
"""

new_list = []
odd = []
even = []
r = range(1,101)

new_list = list(r)

i=1
while i < len(new_list):
    if i%2 == 0:
        odd.append(new_list[i])
    else:
        even.append(new_list[i])
    i+=1


print("\nODD numbers are : " + str(odd) + "\n")
print("EVEN numbers are :" + str(even))

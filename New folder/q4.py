# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:33:44 2018

@author: aksha
"""

a = [10, 'captain', 11.23, 'india', 20, 41.667, 30]
str_list = []
float_list = []
int_list = []
print("\nORIGINAL LIST IS : " + str(a))


i=0
while i < len(a):
    if type(a[i]) == str:
        str_list.append(a[i])
    if type(a[i]) == float:
        float_list.append(a[i])
    if type(a[i]) == int:
        int_list.append(a[i])
    i+=1

print("\nString List is : " + str(str_list))
print("Float List is : " + str(float_list))
print("Integer List is : " +str(int_list))

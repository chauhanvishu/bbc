# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:37:50 2018

@author: aksha
"""

n = int(input("\nEnter number of elements to to entered in a list : "))
l = []
count = 0
delete = []


for i in range(0,n):
    l.append(int(input("Enter a integer value :")))


print("\nList is :" + str(l))
s = int(input("Enter the value to be searched and deleted : "))

for i in range(0,n):
    if l[i] == s:
        delete.append(int(i))
    else:
        continue

print(str(s) + " is present in indexe(s) : " + str(delete))
for i in range(0,len(delete)):
    l.remove(s)


print("\nAfter iteration List is : " + str(l))
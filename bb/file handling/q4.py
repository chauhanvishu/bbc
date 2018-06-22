# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 00:02:30 2018

@author: aksha
"""

with open("sam.txt", "r") as f:
    a = f.readlines()

with open("output.txt", "r") as f:
    b = f.readlines()

i=0
while i<len(a):
    print("From sam.txt   :" + a[i] + "\n" + "from output.txt :" +b[i])
    i+=1


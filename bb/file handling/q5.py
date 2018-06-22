# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 00:02:47 2018

@author: aksha
"""

import random

b=[]
with open("sam2.txt", "w") as f:
    for i in range(10):
        a =random.random()
        b.append(a)
        f.write(str(a) + "\n")

a = b.sort()

with open("OUTPUT2.txt", "w") as f:
    for i in range(len(b)):
        f.write(str(b[i]) + "\n")
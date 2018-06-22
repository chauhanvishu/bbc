# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:36:18 2018

@author: aksha
"""

dic = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16, 'g': 17}
print("\nOriginal Dictionary is :")
print(str(dic) + "\n")
dic_keys = list(dic.keys())
dic_values = list(dic.values())

for x in range(0,len(dic)):
    print(str(dic_keys[x]) + ": " + str(dic_values[x]) + "\n")


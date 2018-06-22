# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 00:02:04 2018

@author: aksha
"""

with open("sam.txt", "r") as f:
    with open("output.txt", "w") as f1:
        for word in f:
            f1.write(word)

print("New copied file created is output.txt")


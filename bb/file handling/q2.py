# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 00:01:16 2018

@author: aksha
"""

from collections import Counter

def word_count(file):
        with open(file) as f:
                return Counter(f.read().split())

print("Number of words in the file with their frequency : ",word_count("sam.txt"))

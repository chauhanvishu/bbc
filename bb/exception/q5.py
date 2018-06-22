# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:38:19 2018

@author: aksha
"""

try:
    raise IndexError
except IndexError:
    print("IndexError  Resolved")


try:
    raise ImportError
except ImportError:
    print("ImportError Resolved")


try:
    raise ValueError
except ValueError:
    print("ValueError  Resolved")

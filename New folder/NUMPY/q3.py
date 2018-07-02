# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 00:17:44 2018

@author: aksha
"""
import numpy as np
from random import *
p = np.random.random((10,20))
q = np.random.random((20,25))
r=np.dot(p,q)
print("First array: \n", p)
print("Second array: \n", q)
print("New Array: n", r)
print("Shape of new matrix: ",np.shape(r))
print("Sum of elements of new array: ",np.sum(r))

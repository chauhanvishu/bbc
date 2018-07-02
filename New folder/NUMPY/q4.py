# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 00:20:20 2018

@author: aksha
"""
import numpy as np
from random import *

Arr = np.random.random((10,1))
print("old array:", Arr)
function = 1/(1+np.exp(-Arr))
print("new array: \n",function)
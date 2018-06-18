# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:32:02 2018

@author: aksha
"""
print ("Enter first age")
first = input()
print ("Enter second age")
second = input()
print ("third age")
third = input()

if first <= second and first <= third:
  print ("youngest is",first)
elif second <= first and second <= third:
  print ("youngest is",second)
elif third <= first and third <= second:
  print ("youngest is",third)
else:
  print ("All are equal")
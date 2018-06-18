# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:52:19 2018

@author: aksha
"""
dictionary = {}

count = 0

while count < 10:
   name = input("Enter your name: ")
   mark = input("Enter your mark out of 100: ")
   if name not in dictionary:
       dictionary[name] = mark
       count = count + 1
   else:
       print("You already used that name, enter an unique name.")


# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 17:10:35 2018

@author: aksha
"""

class Animal:

    def animal_attribute(self):
        print("Base class is inherited")

class Tiger(Animal):

    def __init__(self):
        self.animal_attribute()

obj = Tiger()

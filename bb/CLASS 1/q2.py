# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:50:46 2018

@author: aksha
"""


class Student():
    
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll

    def Display(self):
        print(self.name)
        print(self.roll)
        
P = Student(input("Enter name of student : "), input("Enter his/her roll no : "))
P.Display()

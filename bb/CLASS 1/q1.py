# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:50:22 2018

@author: aksha
"""

class Circle():
    
    def __init__(self,radius):
        self.radius = radius
        
    def  getArea(self):
        print("Area is : " + str(3.14*self.radius*self.radius))
    
    def getCircumference(self):
        print("Circumference is : " + str(self.radius*2*3.14))


P = Circle(float(input("Enter radius : ")))
P.getArea()
P.getCircumference()





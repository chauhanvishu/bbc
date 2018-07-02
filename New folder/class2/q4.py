# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 17:13:04 2018

@author: aksha
"""

class Shape:
    def __init__(self, length , breath):
        self.length = length
        self.breath = breath

    def Area(self):

        print("Area is : " + str(self.length * self.breath))



class Rectangle(Shape):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath


class Square(Shape):

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

A = Rectangle(int(input("Enter length of rectangle : ")), int(input("Enter breath of rectangle : ")))
A.Area()

B = Square(int(input("Enter side of square : ")), int(input("Enter breath of square : ")))
B.Area()
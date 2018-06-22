# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:51:05 2018

@author: aksha
"""


class Temperature():

    def  convertFahrenhiet(self,celsius):
        print("Temperature in Fahrenhiet is : " + str((celsius*(9/5))+32))
        
    def convertCelsius(self,farenhiet):
        print("Temperature in Celsius is : " + str((farenhiet-32)*(5/9)))

P = Temperature()
P.convertFahrenhiet(int(input("Enter temperature in Celcius : ")))
P.convertCelsius(int(input("Enter temperature in Fahrenhiet : ")))


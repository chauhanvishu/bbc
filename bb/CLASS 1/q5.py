# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:52:47 2018

@author: aksha
"""

class Expenditure():

    def __init__(self, expenditure, savings):
        self.expenditure = expenditure
        self.savings = savings

    def Display(self):
        print("\n\nExpenditure is  : " + str(self.expenditure))
        print("Savings is      : " + str(self.savings))
        
    def Cal_TotalSalary(self):
        Expenditure.totalsalary = self.expenditure + self.savings

    def Display_TotalSalary(self):
        print("Total Salary is : " + str(self.totalsalary))

A = Expenditure(input("\n\nEnter Expenditure : "), input("Enter Savings     : "))
A.Display()

A.Cal_TotalSalary()
A.Display_TotalSalary()
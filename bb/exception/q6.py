# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:38:41 2018

@author: aksha
"""

class Error(Exception):
    pass

class AgeTooSmallError(Error):
    def __init__(self):
        print("AgeTooSmallError: WARNING")

while True:
    val = int(input(" age: "))
    try:
        if val < 18:
            raise AgeTooSmallError
        else:
            print("Your age: ",val)
            break
    except AgeTooSmallError:
        print("Age is less than 18. Enter value equal to or greater than 18. Try again!!")

print(" LOOP SE BAHAR")
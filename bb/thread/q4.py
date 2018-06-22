# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:32:11 2018

@author: aksha
"""

import threading
import math

class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global result
        temp = math.factorial(self.num)
        print(str(self.name) + " calculate " + str(self.num) + " factorial  : " + str(temp))
        result += temp

result = 0
threads = []

def test():
    for i in range(1,6):
        t = f(i)
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()

print("Calling Factorial 1 to 5 :\n")
if __name__ == '__main__':
    test()
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:13:14 2018

@author: aksha
"""

import threading
import time

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("\nThread Starting")
        i=1
        while i<=5:
            print(i)
           
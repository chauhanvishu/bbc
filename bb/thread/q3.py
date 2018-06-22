# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:15:09 2018

@author: aksha
"""

import threading
import time

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Thread starting")


threads = ['11', '12', '13', '14', '15']
i = 10
for t in threads:
    t = mythread()
    t.run()
    time.sleep(2)
    print(2*i)
    i=i+1
    print("Thread Ending")

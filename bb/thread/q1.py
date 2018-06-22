# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:11:24 2018

@author: aksha
"""

import threading
import time

t = threading.Thread()
t.start()
print(threading.currentThread().getName())
time.sleep(5)
print("MESSAGE DISPLAYED")

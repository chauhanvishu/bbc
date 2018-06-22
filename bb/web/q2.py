# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:42:08 2018

@author: aksha
"""

import socket
addr1 = socket.gethostbyname('www.yahoo.com')
addr2 = socket.gethostbyname('www.instagram.com')
print("IP Address of yahoo.com: %s\nIP Address of instagram.com: %s " % (addr1, addr2))


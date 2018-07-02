# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:30:02 2018

@author: aksha
"""

from tkinter import *
dict = {'Abc': '3535xxxxx', 'qwe': '5756xxxxxx', 'cvb': '76868xxxxx', 'wer': '5767xxxxx', 'jhg': '46469xxxx'}
tk = Tk()
f = Frame(master=tk)
f.pack()
scroll = Scrollbar(master=f)
scroll.pack(fill=Y, side=RIGHT)
l = Listbox(f, yscrollcommand=scroll.set)
for key in dictionary:
    l.insert(END, '{}'.format(key))
l.pack(side=LEFT)
scroll.config(command = l.yview)

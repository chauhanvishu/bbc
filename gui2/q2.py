# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:31:16 2018

@author: aksha
"""
from tinkter import *
def add():
    dict.update({E1.get(): E2.get()})
    for key in dict.keys():
        print(key)
    i = key
    l.insert(END, i)

btn = Button(master=f, text="ADD", command=add)
btn.pack()
lbl = Label(f,text="Enter name and phone number: ")
lbl.pack()
E1 = Entry(f, text="Name")
E2 = Entry(f, text="Phone No.")
E1.pack()
E2.pack()

tk.mainloop()
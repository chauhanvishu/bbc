# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:21:55 2018

@author: aksha
"""

import tkinter as tk
    

def write_slogan():
    print("Tkinter")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="exit", 
                   fg="red",
                   command=exit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
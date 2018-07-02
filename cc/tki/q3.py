# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:34:45 2018

@author: aksha
"""

import tkinter as Tk
r = Tk()
def change_label():
    label2["text"] = "nice to meet you! "
frame = Tk.Frame(r)
frame.pack()
label2 = Tk.Label(r,text="\nCLICK ONE OF THE BUTTONS\n")
label2.pack()
bottomframe =Tk.Frame(r)
bottomframe.pack(side=Tk.BOTTOM)
stopbutton = Tk.Button(frame, text='Abort', width = 40, fg = 'green', command = r.destroy)
stopbutton.pack(side=Tk.LEFT)
printbutton = Tk.Button(frame, text='Change Label', width = 40, fg = 'yellow', command=change_label)
printbutton.pack(side=Tk.LEFT) 
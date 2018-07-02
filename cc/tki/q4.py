# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:36:43 2018

@author: aksha
"""


tk = Tk()
def display():
    print(e1.get()+ " loves " +e2.get())
Label(tk, text = "Enter your name: ").grid(row=0)
Label(tk, text = "Enter name of favorite person: ").grid(row=1)
e1 = Entry(tk)
e2 = Entry(tk)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
button1 = Button(tk, text='PRINT',width=50,fg='Green',command=display)
button1.grid(row=4,column=1)

m.mainloop()
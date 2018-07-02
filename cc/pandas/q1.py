# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:48:08 2018

@author: aksha
"""

import pandas as pd


data = {'Name':['rahul'],'Age':[23],'mail id':['rahulbg67@gmail.com'],'phone no':['9457xxxxxx']}
df = pd.DataFrame(data)
df.loc[1]=['alok',25,'alokkumar@gmail.com','8126xxxxxx']       
df.loc[2]=['arjun',26,'mahesharjun@gmail.com','97606xxxxx']       
print(df)

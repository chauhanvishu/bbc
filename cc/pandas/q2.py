# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:51:43 2018

@author: aksha
"""
import pandas as pd
df=pd.read_csv('weather.csv')



print(df.head(5))


print(df.head(10))

print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())

print(df.tail(5))

finaldata=[df.iloc[:,2].sum(),
df.iloc[:,2].mean(),
df.iloc[:,2].median(),
df.iloc[:,2].nunique(),
df.iloc[:,2].max(),
df.iloc[:,2].min()]
print(finaldata) 
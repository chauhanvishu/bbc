# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:23:18 2018

@author: aksha
"""

dic={}
a="mississippi"
count1=1
count2=1
count3=1
count4=1
for i in a:
    
    name='m'
    if(i=='m'):
        dic[name]=count1
        count1=count1+1
    
    name='i'
    if(i=='i'):
        dic[name]=count2
        count2=count2+1

    name='s'
    if(i=='s'):
        dic[name]=count3
        count3=count3+1

    name='p'
    if(i=='p'):
        dic[name]=count4
        count4=count4+1




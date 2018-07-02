# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:59:55 2018

@author: aksha
"""
import MySQLdb
db=MySQLdb.connect("localhost","root","2216","DB1")
cursor=db.cursor()

upd ="""UPDATE BOOKS SET GENRE="MYSTERY" 
      WHERE LOCATION='HARIDWAR'"""
try:
    cursor.execute(upd)
    db.commit()
except:
    db.rollback()
db.close()
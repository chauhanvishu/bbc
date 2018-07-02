# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:59:07 2018

@author: aksha
"""
import MySQLdb
db=MySQLdb.connect("localhost","root","2216","DB1")
cursor=db.cursor()

insert1 = """INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE ) 
        VALUES(101, 11, "GODAN","HINDI")"""
try:
    cursor.execute(insert1)
    db.commit()
except:
    db.rollback()

insert2 = """INSERT INTO TITLES( TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLICATION_YEAR ) 
        VALUES(112,"GODAN",1253556,108,2004)"""
try:
    cursor.execute(insert2)
    db.commit()
except:
    db.rollback()

insert3 = """INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,STATE_NUMBER,ZIP_CODE_ID ) 
        VALUES(145,"ZOMATO","RAILWAY ROAD",34665,4)"""
try:
    cursor.execute(insert3)
    db.commit()
except:
    db.rollback()

insert4 = """INSERT INTO ZIP_CODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE) 
        VALUES(3,"HARIDWAR","UK",247663)"""
try:
    cursor.execute(insert4)
    db.commit()
except:
    db.rollback()

insert5 = """INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID ) 
        VALUES(123,120,265)"""
try:
    cursor.execute(insert5)
    db.commit()
except:
    db.rollback()

insert6 = """INSERT INTO AUTHORS(AUTHOR_ID, FIRST_NAME, MIDDLE_NAME,LAST_NAME ) 
        VALUES(111,"HARRY","-","POTAR")"""
try:
    cursor.execute(insert6)
    db.commit()
except:
    db.rollback()

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:58:34 2018

@author: aksha
"""

import MySQLdb
db=MySQLdb.connect("localhost","root","2216","DB1")
cursor=db.cursor()


print("Q1. CREATE the following tables\n")

  
sql="""CREATE TABLE BOOKS 
BOOK_ID INT NOT NULL,
TITLE_ID INT,
LOCATION CHAR(15),
GENRE CHAR(15)
"""

sql2="""CREATE TABLE TITLES 
TITLE_ID INT NOT NULL,
TITLE CHAR(30),
ISBN INT, 
PUBLISHER_ID INT,
PUBLICATION_YEAR INT 
"""

sql3="""CREATE TABLE PUBLISHERS
PUBLISHER_ID INT NOT NULL,
NAME CHAR(30),
STREET_ADDRESS CHAR(30),
SUITE_NUMBER INT,
ZIP_CODE INT
"""

sql4="""CREATE TABLE ZIP_CODES
ZIP_CODE_ID INT NOT NULL,
CITY CHAR(20),
STATE(20),
ZIP_CODE INT
"""

sql5="""CREATE TABLE AUTHORS TITLES
AUTHOR_TITLE_ID INT NOT NULL,
AUTHOR_ID INT,
TITLE_ID INT
"""
sql6="""CREATE TABLE AUTHORS
AUTHOR_ID INT NOT NULL,
FIRST_NAME CHAR(10),
MIDDLE_NAME CHAR(10),
LAST_NAME CHAR(10)
"""

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)

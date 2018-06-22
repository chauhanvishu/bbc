# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:52:32 2018

@author: aksha
"""

class MovieDetails():

    def __init__(self, Moviename, Artistname, Yearofrelease, Ratings):
        self.Moviename = Moviename
        self.Artistname = Artistname
        self.Yearofrelease = Yearofrelease
        self.Ratings = Ratings

    def Display(self):
        print("Movie name is      : " + str(self.Moviename))
        print("Artist name is     : " + str(self.Artistname))
        print("Year of Release is : " + str(self.Yearofrelease))
        print("Ratings is         : " + str(self.Ratings) + "\n\n")

    def Update(self):
        self.Moviename = input("Enter updated Movie name      : ")
        self.Artistname = input("Enter updated Artist name     : ")
        self.Yearofrelease = input("Enter updated Year of release : ")
        self.Ratings = input("Enter updated Ratings         : ")

P = MovieDetails('BARFI','RANBIR KAPPOR', '2012', '89')
P.Display()

P.Update()
P.Display()

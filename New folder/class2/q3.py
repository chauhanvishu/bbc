# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 17:10:47 2018

@author: aksha
"""

class Cop:

    def __init__(self, name, age, work_experience, designation):
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.designation = designation

    def add(self):
        self.name = input(" name : ")
        self.age = input(" age : ")
        self.work_experience = input(" work experience : ")
        self.designation = input(" designation : ")

    def display(self):
        print("Name of cop : " + str(self.name))
        print("Age of cop  : " + str(self.age))
        print("Work experience of cop:  " + str(self.work_experience))
        print("Designation of cop : " + str(self.designation))

    def update(self):
        self.name = input(" name : ")
        self.age = input(" age : ")
        self.work_experience = input(" work experience : ")
        self.designation = input(" designation : ")


class Mission(Cop):
    def add_mission_details(self):
        print("\n cop is ready")

c = Cop('name', 'age', 'work experience', 'designation')
c.add()
c.display()
c.update()
c.display()
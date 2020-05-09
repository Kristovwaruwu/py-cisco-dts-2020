# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:47:55 2020

@author: Kristov
"""

print("2.1.6.11 LAB: Operators and expressions")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
#total jam dalam menit
time = (hour * 60 + mins + dura)
x = int(time / 60) % 24
y = int(time % 60)

print("Duration end in = ", x,":", y)
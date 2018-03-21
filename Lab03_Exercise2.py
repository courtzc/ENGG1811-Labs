# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:49:38 2018

@author: court
"""
a = float(input('Enter angle a'))
b = float(input('Enter angle b'))
c = float(input('Enter angle c'))

if (a + b + c == 180):
    if (a == b and b == c):
        print("That's an Equilateral triangle")
    elif ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        print("That's an Isosceles triangle")
    elif (a != b and b != c and c != a):
        print("That's a Scalene triangle")
    
else: print("That's not a triangle!")
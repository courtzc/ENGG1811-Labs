# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:09:05 2018

@author: court
"""

# Ask the user to input the altitude
region = float(input("How high are we talkin'?"))

# Check if the region is above ground
if (region >=0):

# Calculate which region the altitude is
    if (region > 120):
        print("That's the Thermo-Exosphere!")
    elif (region > 60):
        print("That's the Mesosphere!")
    elif (region > 17):
        print("That's the Stratosphere!")
    else: print("That's the Troposphere!")

# Print error message
else: print("Let's avoid talking about below ground, shall we?")
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:26:10 2018

@author: court
"""

# Set variables
run_again = 'Y'

while (run_again == 'Y' or ' Y'):
# Ask the user to input a real number between 0.0 to 360.0 inclusively
    user = (input('What is your bearing?'))

# Check if the input is a number
    try:
        bearing = float(user)
# Check if number is in range
        if (bearing >=0.0 and bearing <= 360.0):
# Convert the bearing to angle
            if (bearing < 270):
                angle = 90 - bearing
            elif (bearing >= 270):
                angle = 450 - bearing
# Print the value of angle    
            print('Your angle is:', angle)
        else: print('Number out of range, sorry!')
        
# Print error message
    except ValueError:
        print("That's not a number!")
       
    run_again = (input('Would you like to do it again? Y/N'))



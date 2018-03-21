# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:29:06 2018

@author: court
"""

"""

# Sub-task: Write the function for calculating H(z) 


# Specify the z variables 
z = 15
# Spcify the parameters of the function h, k and n 
h = 3
k = 10   
n = 2.2 


# Sub-task: Call the function 
# Sub-task: Print the output of the function 
# Note: You can complete the above two sub-tasks
# in one line or two lines. This is up to you.  
"""
# Function to calculate
def Calculation(z, h, k, n):
    answer = (h*((z**n))/((k**n)+(z**n)))
    return answer

# Variables
z = 15

# Parameters
h = 3
k = 10
n = 2.2

# Call function
answer = Calculation(z, h, k, n)


# Print output
print('The answer is:', answer)
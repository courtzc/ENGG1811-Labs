# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:42:49 2018

@author: court
"""

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
n_list = [27, 102, 1]

# Call function
for n in [n_list]:
 answer = Calculation(z, h, k, n)


# Print output
print('The answer is:', answer)
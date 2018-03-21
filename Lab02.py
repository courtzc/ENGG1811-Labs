# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:05:26 2018

@author: court

@title: Lab02
"""
Exercise 1:
    #assign variables and calculate
    x = 2**3/3**2
    y = 2**(3/5)
    
Exercise 2:
    #error
    The capital of Number needs to be lowercase to match the variable
    
Exercise 3:
    #assign variables
    full_rotation = 360
    angular_speed = 621
    time_taken = 17.5
    
    #calculate rotations and degrees
    degrees_rotated = angular_speed*time_taken
    complete_rotations = degrees_rotated//full_rotation
    angular_position = degrees_rotated%full_rotation
    
    #print results
    print ('full rotations: ', complete_rotations, ', final angular position: ', angular_position)
    full rotations:  30 , final angular position:  67.5
    
    
Exercise 4:
    #import maths library
    import math
    
    #assign math variables
    pi = (math.pi)
    cos = (math.cos)
    sin = (math.sin)
    
    #assign g constant
    g = 9.8
    
    #assign variables
    initial_speed = 80
    initial_angle = pi/6
    time = 5
    
    #compute coordinates
    x_coordinate = '%.2f'% initial_speed*cos(initial_angle)*time
    y_coordinate = initial_speed*sin(initial_angle)*time - 0.5*g*time**2
    
    #print results
    print('x-coordinate at t = 5: ', x_coordinate)
    print('y-coordinate at t = 5: ', y_coordinate)
    
    
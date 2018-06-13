#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Lab

Exercise on simulation
"""
import numpy as np 
import math 

def sim_projectile(time_array,m,c,v0,theta0d): 
    # Constants 
    # Physical constants 
    g = 9.81   # acceleration due to gravity 
    
    # Extract information from time vector 
    len_time_array = len(time_array)  # number of time points
    dt = time_array[1]-time_array[0]  # time increment 
    
    # Initialise storage for positions and velocities
    position_x = np.zeros_like(time_array)
    velocity_x = np.zeros_like(time_array)
    position_y = np.zeros_like(time_array)
    velocity_y = np.zeros_like(time_array)
    
    # initialise velocity at zero time 
    velocity_x[0] = v0*math.cos(math.radians(theta0d));
    velocity_y[0] = v0*math.sin(math.radians(theta0d));
    # initial position is assumed to be (0,0)
    
    # the simulation loop
    for k in range(1,len_time_array): 
        # Update x-position
        position_x[k] = position_x[k-1] + velocity_x[k-1] * dt;   
        # Update y-position
        position_y[k] = position_y[k-1] + velocity_y[k-1] * dt;
        # Compute total speed 
        speed_total = math.sqrt(velocity_x[k-1]**2+velocity_y[k-1]**2);
        # Update x-velocity
        velocity_x[k] = velocity_x[k-1] - c*speed_total*velocity_x[k-1]/m*dt; 
        # Update y-velocity
        velocity_y[k] = velocity_y[k-1] - (c*speed_total*velocity_y[k-1]/m + g)*dt;            
  
    return position_x, position_y 


def find_landing_pos_time(time_array,position_x,position_y,landing_level):
    
    # Replace all the values below the landing level with zero
    position_y[position_y < landing_level] = 0
    
    # Find the place of maximum turning point of the curve
    maximum = np.argmax(position_y)
    
    # Replace all the values before the maximum turning point with zero
    position_y[:maximum] = 0
    
    # Replace all zero values with a value above the landing level
    position_y[position_y == 0] = landing_level+100
    
    # Find the place of minimum value
    minimum = np.argmin(position_y)
    
    # Find the landing position and time
    landing_position = position_x[minimum]
    
    landing_time = time_array[minimum]

    return landing_position,landing_time
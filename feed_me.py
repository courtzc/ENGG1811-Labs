# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:44:50 2018

@author: court
"""
import numpy as np
import matplotlib.pyplot as plt
import sim_projectile_lab_08 as sim

# Problem parameters 
m = 0.145      # mass of the strawberry 
c = 0.0013     # damping coefficient 
v0 = 50        # initial launch speed
theta0d = 35   # initial launch angle 

# Simulation parameters 
dt = 0.01      # time increment 
time_end = 10       # end time of simulation 
time_array = np.arange(0,time_end,dt) # time vector 
print(time_array)

# Simulation to obtain the x- and y-positions
position_x,position_y = sim.sim_projectile(time_array,m,c,v0,theta0d)

# Plot y-position versus x-position 
plt.figure(1)
plt.plot(position_x,position_y)
plt.grid()
plt.xlabel('x-position')
plt.ylabel('y-position')
plt.title('Position of the strawberry')
plt.show()


angle_array = np.arange(20,61,1)
landing_distances = np.zeros_like(angle_array)
landing_times = np.zeros_like(angle_array)

for j in np.arange(len(angle_array)):
    position_x,position_y = sim.sim_projectile(time_array,m,c,v0,angle_array[j])
    landing_distances[j], landing_times[j] = sim.find_landing_pos_time(time_array,position_x,position_y,landing_level = 10)
    
print("landing_distances:", landing_distances)
print("landing_times:", landing_times)

# Plot landing_position vs landing_time
plt.figure(2)
plt.plot(landing_times,landing_distances)
plt.grid()
plt.xlabel('Landing Time')
plt.ylabel('Landing Distances')
plt.title('Landing Distances vs Landing Times')
plt.show()
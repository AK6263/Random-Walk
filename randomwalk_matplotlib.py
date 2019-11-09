# -*- coding: utf-8 -*-
"""

@author: Abhay Kshirsagar
"""

from random import choice
import matplotlib.pyplot as plt
class RandomWalk():
    """A class to generate random walks."""
    def __init__(self, num_points=10000):
        """Initialize attributes of a walk."""
        
        self.num_points = num_points
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        """calculate all the points in the walk"""
        
        #Keep taking Steps until the walk reaches the desired length
        while len(self.x_values)<self.num_points:
            #decide which derection to go and how far in that direction
            x_direction =choice([1,-1])
            x_distance = choice([0,1,2,3,4,5])
            x_step = x_direction * x_distance
            #x_Step and y_step are vectors
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4,5])
            y_step = y_direction*y_distance
            #reject moves that go nowhere.
            if x_step==0 and y_step==0:
                continue
            # Calculate the next x and y values
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
rw = RandomWalk()
rw.fill_walk()
plt.plot(rw.x_values,rw.y_values)
plt.show()

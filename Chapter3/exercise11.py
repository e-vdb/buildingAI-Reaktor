#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:06:16 2021

@author: Emeline

Exercise 11: Real estate price predictions


"""

import numpy as np

# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]

X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    for x in X:
        price = np.dot(x,c)           
        print(price)

predict(X, c)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 13:55:24 2021

@author: Emeline

Exercise 15: Vector distances

"""

import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    distances = [dist(train_item, x_test) for train_item in x_train]
    nearest=np.argmin(distances)
    print(nearest)

nearest(x_train, x_test)

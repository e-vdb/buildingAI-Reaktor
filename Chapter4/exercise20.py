#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:59:20 2021

@author: Emeline

Exercise 20: Logistic regression

"""

import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

coeff=[c1,c2,c3]
def sigmoid(z):
    result=1/(1+math.exp(-z))
    print(result)

# calculate the output of the sigmoid for x with all three coefficients

y_predict=[c@x for c in coeff]
for y in y_predict:
    sigmoid(y)

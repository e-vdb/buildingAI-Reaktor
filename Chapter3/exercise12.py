#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:16:44 2021

@author: Emeline
    
    Exercise 12: Least squares

"""


# beginner level 

def linModel(c,x):
    return c[0]+c[1]*x

def MSE_loss(ytrue,ypred):
    # MSE_loss calculates the mean squared error between the true values of the sample (data)
    # and the predicted values obtained with the neural network (pred)
    error=0
    for count in range(len(ypred)):
        error+=(ytrue[count]-ypred[count])**2
    return error/len(ytrue)


models=[[0.5,3.2],[0,1.9],[7.6,1.9]]
data=[[0,5],[2,9.6],[3.2,13.6]]

dataX=[dataI[0] for dataI in data]
dataY=[dataI[1] for dataI in data]

for model in models:
    predY=[linModel(model, dataXi) for dataXi in dataX]
    print(MSE_loss(dataY, predY))
 
    
# intermediate level 
    
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        sse+=(yi-np.dot(c,xi))**2
    print(sse)

squared_error(X, y, c)


# advance level 

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for count,coeff in enumerate(c):
        sse = 0.0
        for xi, yi in zip(X, y):
            sse+=(yi-np.dot(coeff,xi))**2
        if sse<smallest_error:
            smallest_error=sse
            best_index=count
    print("the best set is set %d" % best_index)


find_best(X, y, c)

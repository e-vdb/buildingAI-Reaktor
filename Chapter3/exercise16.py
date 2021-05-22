#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:32:29 2021

@author: Emeline

Exercise 16: Nearest neighbor

"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3    # classify our test items based on the classes of 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]
        neighbors=np.argsort(distances)
        
        kNeighbors=[neighbors[count] for count in range(k)]
        label_kNeighbors=[y_train[neighbor] for neighbor in kNeighbors]
        label=0
        nbLabel1=np.count_nonzero(label_kNeighbors)
        if nbLabel1>1:
            label=1
        
        # create a line connecting the points for the chart
        for neighbor in kNeighbors:
            lines.append(np.stack((test_item, X_train[neighbor])))

        y_predict[i] = label          
    
    print(y_predict)

main(X_train, X_test, y_train, y_test)

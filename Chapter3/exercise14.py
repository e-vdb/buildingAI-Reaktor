#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 13:33:05 2021

@author: Emeline

Exercise 14: Training data vs test data

"""
import numpy as np
from io import StringIO

# data 

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''
 
def main():
    # simulate reading a file
    data_train_string = StringIO(train_string)
    data_test_string = StringIO(test_string)
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    # read the data in and fit it. the values below are placeholder values
   
    # read in the training data and separate it to x_train and y_train
    dataTrain = np.genfromtxt(data_train_string, skip_header=1)  
    Y_train=dataTrain[:,-1]
    X_train=dataTrain[:,0:-1]
    
    # fit a linear regression model to the data and get the coefficients
    c=np.linalg.lstsq(X_train, Y_train)[0]
    
    # read in the test data and separate x_test from it
    dataTest=np.genfromtxt(data_test_string, skip_header=1)
    X_test=dataTest[:,0:-1]
    
    # print out the linear regression coefficients
    print(c)
    
    # this will print out the predicted prics for the two new cabins in the test data set
    print(X_test @ c)


main()

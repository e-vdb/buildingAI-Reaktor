#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:43:19 2021

@author: Emeline

Exercise 17: Bag of words

"""

import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def manhattan_distance(listA,listB):
    sum=0
    for listA_item,listB_item in zip(listA,listB):
        sum+=np.absolute(listA_item-listB_item)
    return sum

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    
    for i in range(N):
        for j in range(N):
            if i!=j:
                dist[i][j]=manhattan_distance(data[i],data[j])
            else:
                dist[i][j]=np.inf
    
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)

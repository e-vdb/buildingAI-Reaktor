#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:54:15 2021

@author: Emeline
"""

import random

# intermediate level

def answerInt():
    prob = 0.80
    if random.random() < prob:
        print('dog')
    else:
        print('cat')
answerInt()


# advance level
def answerAdv():
    
    favourite = "dogs"
    prob=random.random()
    if prob>0.8 and prob<0.9:
        favourite='bats'
    elif prob>0.9:
        favourite='cats'
    print("I love " + favourite) 


answerAdv()

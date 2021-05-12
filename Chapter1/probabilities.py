#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:54:15 2021

@author: Emeline
"""

import random

def main():
    prob = 0.80
    if random.random() < prob:
        print('dog')
    else:
        print('cat')
main()
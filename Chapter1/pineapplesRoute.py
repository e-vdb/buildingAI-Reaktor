#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:07:55 2021

@author: Emeline

Exercice 1 : Listing pineapple routes
"""
# beginner level exercise

def factorial(n):
    while n>1:
        return n*(factorielle(n-1))
    if n==1:
        return n

print(factorial(3))

#  intermediate level exercise
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    nb=0
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    if set(route) == set(range(5)):
                    # do not modify the print statement
                        print(' '.join([portnames[i] for i in route]))
                       
main()

# advance level exercise
def permutations(route, ports):
    if len(ports)==0:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]],ports[:i]+ports[i+1:])
            
permutations([0], list(range(1, len(portnames))))


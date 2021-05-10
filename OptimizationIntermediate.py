#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:07:55 2021

@author: Emeline
"""

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    nb=0
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    
                    allPorts=True
                    for i in range(1,5):
                        if i not in route:
                            allPorts=False
                    if allPorts:
                    # do not modify the print statement
                        print(' '.join([portnames[i] for i in route]))
                        nb+=1
    return nb
nombre=main()
print(nombre)

def solution():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
    nb=0
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    
                    if set(route) == set(range(5)):

                        print(' '.join([portnames[i] for i in route]))
                        nb+=1

main()


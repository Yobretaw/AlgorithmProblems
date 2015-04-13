import sys
import os
import math
import imp

from stack import Stack

"""
    ============================================================================================
    You are given a series of buildings that have windows facing west. The buildings are in a
    straight line, and any building which is to the east of a building of equal or grater height
    cannot view the sunset.

    Design an algorithm that processes buildings in east-to-west order and returns the set of 
    buildings which view the sunset. Each building is specified by its height.
    ============================================================================================
"""
def buildings_with_sunset(l):
    if not l or len(l) == 1:
        return l

    s = Stack()
    for h in l:
        while not s.empty() and h >= s.top():
            s.pop()
        s.push(h)

    return s.to_array()

#l = [1, 2, 3, 4, 5, 6, 7, 8]
#print buildings_with_sunset(l[::-1])
#print buildings_with_sunset(l)

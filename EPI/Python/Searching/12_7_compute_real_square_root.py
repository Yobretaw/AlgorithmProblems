import sys
import os
import math
import imp
import random

epsilon = 10 ** -12

"""
    Implement a function which takes as input a floating point value and returns
    its square root
"""
def compute_real_square_root(x):
    x = float(x)
    if x < 1.0:
        l, r = x, 1.0
    else:
        l, r = 1.0, x

    while compare(l, r):
        mid = l + (r - l) / 2
        if compare(mid ** 2, x) == 0:
            return mid
        elif compare(mid ** 2, x) < 0:
            l = mid
        else:
            r = mid
    return l

def compare(a, b):
    if abs(a - b) > epsilon:
        return -1 if a < b else 1
    else:
        return 0

#for i in range(1, 100):
#    print compute_real_square_root(i)

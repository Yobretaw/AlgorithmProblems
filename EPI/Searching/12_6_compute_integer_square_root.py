import sys
import os
import math
import imp
import random

"""
    Write a function which takes a nonnegative integer and returns the largest
    integer whose square is less than or equal to the given integer.
"""
def find_largest_integer(x):
    if x < 2:
        return x

    l, r = 1, x / 2
    while l < r:
        mid = l + (r - l) / 2
        if mid ** 2 <= x and (mid + 1) ** 2 > x:
            return mid
        elif mid ** 2 > x:
            r = mid
        else:
            l = mid + 1
    return -1

#print find_largest_integer(16)
#print find_largest_integer(300)

import sys
import os
import math

"""
    Implement int sqrt(int x).

    Compute and return the square root of x.
"""
def my_sqrt(x):
    start = 0
    end = x
    while start <= end:
        mid = (start + end) / 2
        if mid ** 2 <= x and (mid + 1) ** 2 > x:
            return mid
        elif mid ** 2 > x:
            end = mid - 1
        else:
            start = mid + 1


"""
    Assume the root is r. If i > r, then x/i < r < i, so j < i, so we should return i when j >= i.
"""
def my_sqrt_newton(x):
    i = x
    while i != 0:
        j = (i + x / i) / 2
        if j >= i:
            return i
        i = j
    return i

#for i in range(1, 100):
#    print i, int(i ** 0.5), my_sqrt(i)

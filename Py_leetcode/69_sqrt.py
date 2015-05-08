import sys
import os
import math

"""
    Implement int sqrt(int x).

    Compute and return the square root of x.
"""
def my_sqrt(x):
    if x < 2:
        return x

    res = 1
    while res ** 2 < x:
        m = 1
        while (res + m << 1) ** 2 < x:
            m >>= 1
        res += m
    return res

for i in range(1, 1000):
    print i, int(i ** 0.5), my_sqrt(i)

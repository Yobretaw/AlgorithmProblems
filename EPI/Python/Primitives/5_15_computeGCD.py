import sys
import os
import re
import math


"""
    Naive Implementation
"""
def GCD(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x > y:
        return GCD(x - y, y)
    else:
        return GCD(x, x - y)


"""
    Fast Implementation: O(logx + logy)
"""
def GCD_fast(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif not (x & 1) and not (y & 1):    # both x and y are even
        return GCD_fast(x >> 1, y >> 1) << 1
    elif not (x & 1) and y & 1:         # x is even, y is odd
        return GCD_fast(x >> 1, y)
    elif x & 1 and not(y & 1):          # x is odd, y is even
        return GCD_fast(x, y >> 1)
    elif x > y:                         # both are odd, x is larger than y
        return GCD_fast(x - y, y)
    else:
        return GCD_fast(x, y - x)            # both are odd, y is larger


#for i in range(0, 1000):
#    for j in range(0, 500):
#        #print GCD(i, j)
#        print i, " ", j, " ", GCD_fast(i, j)


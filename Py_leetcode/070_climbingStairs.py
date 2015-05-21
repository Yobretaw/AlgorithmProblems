import sys
import os
import math

"""
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def count_ways(n):
    if n == 1:
        return 1

    a = 1
    b = 1
    while n > 0:
        a, b = b, a + b
        n -= 1

    return a

#for i in range(1, 11):
#    print count_ways(i)

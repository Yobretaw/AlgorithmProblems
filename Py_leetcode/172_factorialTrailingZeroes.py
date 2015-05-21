import sys
import math

"""
    Given an integer n, return the number of trailing zeros in n!.

    Note: Your solution should be in logarithmic time complexity.
"""
def trailing_zeros(n):
    res = 0
    power = 1
    while 5 ** power <= n:
        res += n / (5 ** power)
        power += 1
    return res

#print trailing_zeros(4383)

import sys
import os
import re
import math


"""
    The number of multiplication is at most twice the number of bits to the right
    of the MSB of y that are set to 1. This implied O(n) complexity, where n is
    the number of bits needed to represent y
"""
def power(x, y):
    result = 1

    if y < 0:
        y = -y
        x = 1 / x

    while y:
        if y & 1:
            result *= x
        
        x *= x
        y >>= 1

    return result


def power2(x, y):
    if y < 0:
        y = -y
        x = 1 / x
    return power2Help(x, y)

def power2Help(x, y):
    if y < 2:
        return 1 if x == 0 else x

    curr = power2(x, y/2)
    return curr * curr * (x if y & 1 else 1)


print power(11.23, 12)
print power2(11.23, 12)
print 11.23 ** 12
print "-"*50
print power(11.23, -12)
print power2(11.23, -12)
print 11.23 ** -12

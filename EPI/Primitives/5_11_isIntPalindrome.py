import sys
import os
import re
import math
import random

"""
    Write a function that takes an integer and determine if that integer's
    representation as a decimal string is a palindrome
"""
def isPal(x):
    if x < 0:
        return False

    m = 1
    while 10 * m <= x:
        m *= 10

    while x >= 10:
        if x / m != x % 10:
            return False

        x %= m
        x /= 10
        m /= 10

    return True


for i in range(0, 1000):
    print i, " ", isPal(i)


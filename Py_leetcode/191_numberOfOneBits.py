import sys
import os
import re
import math

"""
    Write a function that takes an unsigned integer and returns the number of '1' bits it
    has (also known as the Hamming weight).

    For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
    so the function should return 3.
"""
def number_one_bits(n):
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res

#print number_one_bits(11)

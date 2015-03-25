import sys
import os
import re
import math

"""
    The appraoch is to swap the first two consecutive bits that diff
    This appraoch works because we want to change bits taht are as far
    the right as possible
"""
def closeintSameBits(x):
    for i in range(0, 63):
        if ((x >> i) & 1) ^ ((x >> (i + 1) & 1)):
            x ^= ((1 << i) | (1 << (i + 1)))
            return x

    # raise error if all bits of x are 0s or 1s
    raise Exception("all bits are 0s or 1s")



print closeintSameBits(7)
print closeintSameBits(2)

# should raise exeption
print closeintSameBits(0)

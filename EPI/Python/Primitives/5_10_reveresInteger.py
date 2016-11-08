import sys
import os
import re
import math

def reverse(x):
    if x < 10:
        return x

    is_neg = x < 0

    x = abs(x)
    result = 0
    while x:
        result *= 10
        result += x % 10
        x /= 10

    return -result if is_neg else result

for i in range(0, 1000):
    print reverse(i)

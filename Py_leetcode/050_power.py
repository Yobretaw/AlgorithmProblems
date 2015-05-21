import sys
import math
from collections import defaultdict

"""
    Implement pow(x, n).
"""
def power(x, n):
    result = 1

    if n < 0:
        n = -n
        x = 1 / x

    while n:
        if n & 1:
            result *= x
        
        x *= x
        n >>= 1

    return result

for i in range(0, 10):
    if not power(2, i) == 2 ** i:
        print i, power(2, i), 2 ** i

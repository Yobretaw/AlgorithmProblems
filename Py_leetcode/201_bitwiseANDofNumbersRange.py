import sys
import os
import re
import math
from collections import deque

"""
    Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers
    in this range, inclusive.

    For example, given the range [5, 7], you should return 4.
"""
def range_bitwise_AND(m, n):
    res = m & n
    mask = 1
    while mask < n - m:
        if res & mask:
            res -= res & mask
        mask <<= 1
    return res

def range_bitwise_AND_2(m, n):
    if m == n:
        return m

    # The highest bit of 1 in diff is the highest changed bit.
    diff = m ^ n

    # idx is the index of the highest changed bit. Starting at 1.
    idx = int(math.log(diff) / math.log(2)) + 1

    # Eliminate the changed part
    return (m >> idx) << idx

print range_bitwise_AND_2(1, 4)
print range_bitwise_AND_2(5, 7)
print range_bitwise_AND_2(4, 5)

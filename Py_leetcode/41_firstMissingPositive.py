import sys
import math
from collections import defaultdict

"""
    Given an unsorted integer array, find the first missing positive integer.

    For example,
    Given [1,2,0] return 3,
    and [3,4,-1,1] return 2.

    Your algorithm should run in O(n) time and uses constant space.
"""
def first_missing_positive(a):
    if not a:
        return 1

    i = 0
    n = len(a)
    while i < len(a):
        while 0 < a[i] <= n and a[i] != i + 1 and a[i] != a[a[i] - 1]:
            a[a[i] - 1], a[i] = a[i], a[a[i] - 1]
        i += 1

    for i in range(0, n):
        if a[i] != i + 1:
            return i + 1

    return n + 1

#a = [1, 2, 0]
#a = [3, 4, -1, 1]
#a = [1, 1]
#print(first_missing_positive(a))

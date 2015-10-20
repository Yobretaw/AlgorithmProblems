import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function that which takes as input a set of integers represented
    by an array, and returns the size of a largest subset of integers in the
    array having the property that if two integers are in the subset, then so
    are all integers between them.
    
    For example, if the input is <3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8>, the
    biggest contained range is <-2, -1, 0, 1, 2, 3>, so you should return
    6.
"""

# Brute force: O(nlogn)
def find_longest_subarray_contained_range(a):
    n = len(a)
    if n < 2:
        return max(a) - min(a) + 1

    a.sort()
    start = end = 0
    i = 0
    for idx in range(1, n):
        if a[idx] != a[idx - 1] + 1:
            i = idx

        if (idx - i + 1) > (end - start + 1):
            start, end = i, idx

    return end - start + 1


# O(n)
def find_longest_subarray_contained_range2(a):
    n = len(a)
    if n < 2:
        return max(a) - min(a) + 1

    m = { v : 0 for v in a }

    seen = set()
    max_len = 0
    for k in m.keys():
        if k in seen:
            continue

        seen.add(k)

        l = k - 1
        while l in m:
            seen.add(l)
            l -= 1
        
        h = k + 1
        while h in m:
            seen.add(h)
            h += 1

        max_len = max(max_len, h - l - 1)

    return max_len


if __name__ == '__main__':
    a = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]
    print find_longest_subarray_contained_range(a)
    print find_longest_subarray_contained_range2(a)

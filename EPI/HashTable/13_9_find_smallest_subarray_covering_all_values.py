import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function which takes an array of strings and a set of strings and
    return the indices of the starting and ending index of a shortest subarray
    of the given array that "covers" the set, i.e., contains all strings in the
    set.
"""
def find_smallest_subarray_convering_set(arr, s):
    if len(arr) < len(s):
        return -1, -1

    pos = {}
    for i, v in enumerate(arr):
        pos[v] = i

    l, r = 0, len(arr) - 1
    for ss in s:
        if not ss in pos:
            return -1, -1
        if pos[ss] < l:
            l = pos[ss]
        elif pos[ss] > r:
            r = pos[ss]

    return l, r


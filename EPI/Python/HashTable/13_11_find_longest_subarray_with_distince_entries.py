import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function that takes an array and returns the lenght of longest
    subarray with the property that all its elements are distinct.
"""
def find_longest_subarray_without_dupilcates(s):
    n = len(s)
    if n < 2:
        return s

    i = 0
    start, end = 0, -1
    latest_pos = {}
    for j, char in enumerate(s):
        if char in latest_pos:
            i = max(i, latest_pos[char] + 1)

        latest_pos[char] = j

        if (j - i + 1) > (end - start + 1):
            start, end = i, j

    return s[start:end+1]


if __name__ == '__main__':
    print find_longest_subarray_without_dupilcates('geeksforgeeks')

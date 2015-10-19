import os
import math
import sys
from collections import defaultdict, Counter

"""
    Write a function which takes an array of strings and a set of strings and
    return the indices of the starting and ending index of a shortest subarray
    of the given array that "covers" the set, i.e., contains all strings in the
    set.

    ====
     
    Same as Leetcode: Minimum Window Substring
"""
def find_smallest_subarray_covering_set(s, t):
    if not t or not s or len(s) < len(t):
        return ""

    m, n = len(s), len(t)
    allchar = Counter(t)
    seen = defaultdict(int)

    start, end = 0, sys.maxint
    count = 0

    i = j = 0
    while j < m:
        while j < m and count < n:
            if s[j] in allchar:
                if seen[s[j]] < allchar[s[j]]:
                    count += 1
                seen[s[j]] += 1
            j += 1

        if count < n:
            break

        while i < j:
            if not s[i] in allchar:
                i += 1
            elif seen[s[i]] > allchar[s[i]]:
                seen[s[i]] -= 1
                i += 1
            else:
                if (j - i) < (end - start):
                    start, end = i, j
                break

        if i < j:
            seen[s[i]] -= 1
            i += 1
            count -= 1

    if end == sys.maxint:
        return ''
    return s[start:end]


if __name__ == '__main__':
    print find_smallest_subarray_convering_set('ADOBECODEBANC','ABC')
    print find_smallest_subarray_convering_set('aa','a')
    print find_smallest_subarray_convering_set('aa','ab')

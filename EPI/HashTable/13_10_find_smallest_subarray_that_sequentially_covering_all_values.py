import os
import math
import sys
from collections import defaultdict, Counter

"""
    Same as Leetcode: Minimum Window Substring, except for that the order of
    characters matters.
"""
#def find_smallest_subarray_sequentially_covering_set(s, t):
#    if not t or not s or len(s) < len(t):
#        return ""

#    pos = defaultdict(list)
#    for i, c in enumerate(s):
#        pos[c].append(i)


#    start, end = 0, sys.maxint
#    exit = False
#    old_idx = {c:-1 for c in t}

#    for first_idx, first_pos in enumerate(pos[t[0]]):
#        prev_pos = first_pos
#        old_idx[t[0]] = first_idx

#        for i in range(1, len(t)):
#            next_char = t[i]
#            next_idx = old_idx[next_char] + 1
#            arr = pos[next_char]

#            while next_idx < len(arr) and arr[next_idx] < prev_pos:
#                next_idx += 1

#            if next_idx >= len(arr):
#                exit = True
#                break

#            old_idx[next_char] = next_idx
#            prev_pos = arr[next_idx]

#        if exit:
#            break

#        if (prev_pos - first_pos) < (end - start):
#            start, end = first_pos, prev_pos 
#        if end - start + 1 == len(t):
#            break

#    return s[start:end + 1]


def find_smallest_subarray_sequentially_covering_set(s, t):
    if not t or not s or len(s) < len(t):
        return ""

    pos = defaultdict(list)
    for i, c in enumerate(s):
        pos[c].append(i)


    start, end = 0, sys.maxint
    exit = False
    old_idx = {c:-1 for c in t}

    prev_pos = 0
    for i in range(0, len(t)):
        next_char = t[i]
        next_idx = old_idx[next_char] + 1
        arr = pos[next_char]

        while next_idx < len(arr) and arr[next_idx] < prev_pos:
            next_idx += 1

        if next_idx >= len(arr):
            break

        old_idx[next_char] = next_idx
        prev_pos = arr[next_idx]

    if (prev_pos - first_pos) < (end - start):
        start, end = first_pos, prev_pos 
    if end - start + 1 == len(t):
        break

    return s[start:end + 1]


if __name__ == '__main__':
    print find_smallest_subarray_sequentially_covering_set('ADOBECODEBANC','ABC')
    print find_smallest_subarray_sequentially_covering_set('ADOBECODEBANC','BC')
    print find_smallest_subarray_sequentially_covering_set('FACAI','AA')
    print find_smallest_subarray_sequentially_covering_set('FACAI','A')
    print find_smallest_subarray_sequentially_covering_set('FACAI','FACAI')

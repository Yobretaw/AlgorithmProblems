import os
import math
import sys
from collections import defaultdict, Counter

"""
    Same as Leetcode: Minimum Window Substring, except for that the order of
    characters matters.
    
    Duplicates are allowed in keywords
"""
def find_smallest_subarray_sequentially_covering_set(s, t):
    if not t or not s or len(s) < len(t):
        return ""

    pos = defaultdict(list)
    for i, c in enumerate(s):
        pos[c].append(i)


    start, end = 0, sys.maxint
    exit = False
    old_idx = {c:-1 for c in t}

    for first_idx, first_pos in enumerate(pos[t[0]]):
        prev_pos = first_pos
        old_idx[t[0]] = first_idx

        for i in range(1, len(t)):
            next_char = t[i]
            next_idx = old_idx[next_char] + 1
            arr = pos[next_char]

            while next_idx < len(arr) and arr[next_idx] < prev_pos:
                next_idx += 1

            if next_idx >= len(arr):
                exit = True
                break

            old_idx[next_char] = next_idx
            prev_pos = arr[next_idx]

        if exit:
            break

        if (prev_pos - first_pos) < (end - start):
            start, end = first_pos, prev_pos 
        if end - start + 1 == len(t):
            break

    return s[start:end + 1]


"""
    Duplicates not allowed in keywords characters
"""
def find_smallest_subarray_sequentially_covering_set_without_duplicates(s, t):
    if not t or not s or len(s) < len(t):
        return ""

    n = len(t)

    char_to_idx = { t[i] : i for i in range(n) }
    latest_occurence = [-1] * n
    shortest_subarray_length = [sys.maxint] * n

    res = None
    for i, c in enumerate(s):
        if not c in char_to_idx:
            continue

        idx = char_to_idx[c]

        # first keyword character, start of a subarray
        if idx == 0:
            shortest_subarray_length[idx] = 1
        elif shortest_subarray_length[idx - 1] != sys.maxint:
            distance_to_previous_char = i - latest_occurence[idx - 1]
            shortest_subarray_length[idx] = \
                shortest_subarray_length[idx - 1] + distance_to_previous_char

        latest_occurence[idx] = i
        
        if idx == n - 1 \
                and (
                        res == None or \
                        shortest_subarray_length[-1] < (res[1] - res[0] + 1)
                    ):
            res = (i - shortest_subarray_length[-1] + 1, i)

    print s[res[0]:res[1]+1]
    return res


if __name__ == '__main__':
    print find_smallest_subarray_sequentially_covering_set('ADOBECODEBANC','ABC')
    print find_smallest_subarray_sequentially_covering_set_without_duplicates('ADOBECODEBANC','ABC')
    print find_smallest_subarray_sequentially_covering_set('ADOBECODEBANC','BC')
    print find_smallest_subarray_sequentially_covering_set('FACAI','AA')
    print find_smallest_subarray_sequentially_covering_set('FACAI','A')
    print find_smallest_subarray_sequentially_covering_set('FACAI','FACAI')

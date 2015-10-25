import sys
import math
import itertools
import string
from collections import Counter


"""
    You are given a set of closed integers. Design an efficient algorithm
    for finding a minimum number of numbers that cover all the intervals.
"""
def smallest_cover_numbers(intervals):
    n = len(intervals)
    if n < 2:
        return n

    endpoints = []
    endpoints.extend([(i, e[0], 0) for i, e in enumerate(intervals)])
    endpoints.extend([(i, e[1], 1) for i, e in enumerate(intervals)])

    def compare_func(a, b):
        if a[2] == b[2]:
            return a[1] - b[1]
        elif a[2]:
            return 1 if a[1] >= b[1] else -1
        else:
            return -1 if a[1] <= b[1] else 1

    # sort all endpoints
    endpoints.sort(cmp=compare_func)

    seen = set()
    curr_val = None
    res = []
    j = 0

    for i in range(len(endpoints)):
        p = endpoints[i]
        if p[0] in seen:
            continue
        elif not p[2]:
            # open interval endpoint
            curr_val = p[1]
        else:
            res.append(curr_val)
            while j <= i:
                seen.add(endpoints[j][0])
                j += 1
    return res


if __name__ == '__main__':
    intervals = [
        (0, 3),
        (2, 6),
        (3, 4),
        (6, 9)
    ]
    print smallest_cover_numbers(intervals)

    intervals = [
        (1, 5),
        (2, 7),
        (4, 5),
        (6, 10),
        (8, 9),
        (9, 17),
        (11, 13),
        (12, 15),
        (14, 15)
    ]
    print smallest_cover_numbers(intervals)

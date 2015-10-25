import sys
import math
import itertools
import string
from collections import Counter


"""
    Write a function which takes as input an array of disjoint closed intervals
    with integer endpoints, sorted by increasing order of left endpoint, and an
    interval to be added, and return the union of the intervals in the array
    and the added interval. Your result should be expressed as as union of disjoint
    intervals sorted by left endpoint.
"""
def add_interval(intervals, interval):
    intervals = list(intervals)
    n = len(intervals)
    if not n:
        return [interval]
    elif interval[1] < intervals[0][0]:
        return [interval] + intervals
    elif interval[0] > intervals[-1][1]:
        return intervals + [interval]

    i, j, = 0, n
    mid = 0
    while i < j:
        mid = i + (j - i) / 2
        if mid == 0 and interval[0] <= intervals[0][0] \
            or mid == n - 1 and interval[0] >= intervals[mid][0] \
            or intervals[mid][0] <= interval[0] <= intervals[mid + 1][0]:
            break
        elif intervals[mid][0] > interval[0]:
            j = mid
        else:
            i = mid + 1

    start = end = mid
    while end < n and intervals[end][0] <= interval[1]:
            end += 1

    start_val = min(intervals[start][0], interval[0])
    end_val = max(intervals[end - 1][1], interval[1])
    intervals[start:end] = [(start_val, end_val)]

    return intervals

A = [
    (-4, -1),
    (0, 2),
    (3, 6),
    (7, 9),
    (11, 12),
    (14, 17)
]
print add_interval(A, (1, 8))
print add_interval(A, (-6, -5))
print add_interval(A, (-6, -4))
print add_interval(A, (-5, 16))
print add_interval(A, (-5, 18))
print add_interval(A, (18, 19))

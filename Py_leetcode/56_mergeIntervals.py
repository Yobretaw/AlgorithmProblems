import sys
import os
import math

"""
    Given a collection of intervals, merge all overlapping intervals.

    For example,
    Given [1, 3], [2, 6], [8, 10], [15, 18], 
    return [1, 6], [8, 10], [15, 18].
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge_intervals(intervals):
    n = len(intervals)
    
    if n < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    res = []
    curr_interval = intervals[0]
    for i in range(1, n):
        next_interval = intervals[i]
        if curr_interval.end < next_interval.start:
            res.append(curr_interval)
            curr_interval = next_interval
        else:
            curr_interval.end = max(curr_interval.end, next_interval.end)

    res.append(curr_interval)
    return res


#intervals = [Interval(c[0], c[1]) for c in [[1, 3], [2, 6], [8, 10], [15, 18]]]
#for interval in merge_intervals(intervals):
#    print interval.start, interval.end

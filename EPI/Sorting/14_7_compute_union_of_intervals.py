import sys
import math
import itertools
import string
from collections import Counter


"""
    Design an algorithm that takes as input a set of intervals, and outputs
    their union expressed as a set of disjoint intervals.

    The intervals may be open or closed at either end.
"""
class Interval:
    def __init__(self, start, end, start_open, end_open):
        self.start = start
        self.end = end
        self.start_open = start_open
        self.end_open = end_open

    def merge(self, other):
        if self.end < other.start or \
                self.start > other.end or \
                self.end == other.start and self.end_open and other.start_open or \
                self.start == other.end and self.start_open and other.end_open:
                    # can not merge
                    return None
        else:
            if self.start != other.start:
                self.start_open = self.start_open if self.start < other.start else other.start_open
            else:
                self.start_open &= other.start_open

            if self.end != other.end:
                self.end_open = self.end_open if self.end > other.end else other.end_open
            else:
                self.end_open &= other.end_open

            self.start = min(self.start, other.start)
            self.end = max(self.end, other.end)

            return self

    def __repr__(self):
        return '{start_bracket}{start}, {end}{end_bracket}'.format(**{
            'start_bracket': '(' if self.start_open else '[',
            'start': str(self.start),
            'end': str(self.end),
            'end_bracket': ')' if self.end_open else ']'
        })


def union_intervals(intervals):
    n = len(intervals)
    if n < 2:
        return intervals
    
    for i in range(n - 1):
        res = intervals[i].merge(intervals[i + 1])
        if not res:
            continue
        else:
            intervals[i] = None
            intervals[i + 1] = res
    return filter(None, intervals)


if __name__ == '__main__':

    intervals = [
        Interval(0, 3, True, True),
        Interval(1, 1, False, False),
        Interval(2, 4, False, False),
        Interval(3, 4, False, True),
        Interval(5, 7, False, True),
        Interval(7, 8, False, True),
        Interval(8, 11, False, True),
        Interval(9, 11, True, False),
        Interval(12, 14, False, False),
        Interval(12, 16, True, False),
        Interval(13, 15, True, True),
        Interval(16, 17, True, True)
    ]

    for i in union_intervals(intervals):
        print i

import os
import math
import sys
from collections import defaultdict, Counter
from heapq import *
from fractions import gcd

"""
    You are given a set of points in the plane. Each point has integer coordinates.
    Design an algorithm for computing a line that contains the maximum number of
    points in the set.
"""
class Rational:
    def __init__(self, numerator, denominator):
        if numerator == 0:
            self.t = (0, 1)
        elif denominator == 0:
            self.t = (1, 0)
        else:
            d = gcd(numerator, denominator)
            self.t = (numerator / d, denominator / d)
    
    def __eq__(self, other):
        return self.t == other.t

    def __hash__(self):
        return hash(self.t)

    def __repr__(self):
        return str(self.t)


class Line:
    def __init__(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        k = Rational(y2 - y1, x2 - x1)
        b = Rational(x2 * y1 - x1 * y2, x2 - x1)
        self.t = (k, b)

    def __eq__(self, other):
        return self.t == other.t

    def __hash__(self):
        return hash(self.t)

    def __repr__(self):
        return str(self.t)


def find_line_through_most_points(pts):
    d = defaultdict(set)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d[Line(pts[i], pts[j])].add(pts[i])
            d[Line(pts[i], pts[j])].add(pts[j])

    max_line = None
    max_count = 0
    for k, v in d.iteritems():
        if len(v) > max_count:
            max_count = len(v)
            max_line = k
    return max_line

#pts = [
#    (1, 3),
#    (2, 5),
#    (3, 7),
#    (4, 9),
#    (3, 4),
#    (9, 4)
#]
#print find_line_through_most_points(pts)

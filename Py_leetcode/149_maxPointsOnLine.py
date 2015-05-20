import sys
import os
import math
from collections import defaultdict

"""
    Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
class Point:
    def __init__(self, x, y):
        self.x = x if x else 0
        self.y = y if y else 0


def max_points(points):
    n = len(points)
    if n < 2:
        return n

    res = 0
    for i in range(0, len(points)):
        p = points[i]
        local = 1
        vertical = 1
        duplicates = 0
        m = {}
        for j in range(i + 1, len(points)):
            q = points[j]
            if p.x == q.x:
                if p.y == q.y:
                    duplicates += 1
                else:
                    vertical += 1
            else:
                slope = 1.0 * (p.y - q.y) / (p.x - q.x)
                try:
                    m[slope] += 1
                except KeyError:
                    m[slope] = 2
                local = max(local, m[slope])
        res = max(res, local + duplicates, vertical + duplicates)
    return res


#p = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
#p = [Point(c[0], c[1]) for c in p]
#print max_points(p)

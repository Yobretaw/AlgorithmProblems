import sys
import os
import math
import imp
import random
from heapq import *

"""
    Consider a plane containing billions of points, and their coordinates are
    stored in a file.

    How would you compute the k stars which are closest to the origin?

    ==========

    Time: O(nlogk)
    Space: O(k)
"""
def compute_k_closest(points, k):
    h = []
    points = map(lambda x: -x, points)

    for i in range(k):
        h.append(points[i])

    for i in range(k, len(points)):
        h.append(points[i])
        heapify(h)
        heappop(h)

    return -heappop(h)

l = random.sample([i for i in range(2000)], 2000)
print compute_k_closest(l, 1)
print compute_k_closest(l, 42)
print compute_k_closest(l, 1024)
print compute_k_closest(l, 1999)

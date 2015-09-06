import sys
import os
import math
import imp
import random
from heapq import *

"""
    Given a max-heap, represented as an array A, design an algorithm that computes
    the k largest elements stored in the heap. You cannot modify the heap. For
    example, if the heap is [561, 314, 401, 28, 156, 359, 271, 11, 3], the 4 largest
    elements are 561, 314, 401 and 359.
"""
def compute_k_largest_elements(h, k):
    n = len(h)
    if k >= n or not h:
        return h

    q = [-h[0]]
    m = { k:v for k, v in zip(h, range(n)) }
    res = []
    while q and len(res) < k:
        v = -heappop(q)
        res.append(v)

        i = m[v]
        a = 2 * i + 1
        b = 2 * i + 2
        if a < n:
            heappush(q, -h[a])
        if b < n:
            heappush(q, -h[b])
        else:
            pass
    return res

l = [561, 314, 401, 28, 156, 359, 271, 11, 3]
print compute_k_largest_elements(l, 1)
print compute_k_largest_elements(l, 2)
print compute_k_largest_elements(l, 3)
print compute_k_largest_elements(l, 4)
print compute_k_largest_elements(l, 5)
print compute_k_largest_elements(l, 6)
print compute_k_largest_elements(l, 7)
print compute_k_largest_elements(l, 8)

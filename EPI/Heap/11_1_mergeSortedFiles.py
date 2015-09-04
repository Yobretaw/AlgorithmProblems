import sys
import os
import math
import imp
from heapq import *

"""
    Design an algorithm that takes a set of files each containing increasing integers,
    and writes a single file which contains the integers appear in all input files, in
    increasing order. Each file are of the order of 5 - 100 mega bytes. There will be
    at most 1000 files.

    The algorithm should use very little RAM, ideally of the order of a few kilobytes.

    ========

    Let k be the number of input arrays. Then there are no more than k elements in the
    min-heap. Both extract-min and insert takes O(logk) time. Hence, we do the merge
    in O(nlogk) time, where n is the total number of elements in the input. The space
    complexity is O(k) beyond the space needed to write the final result.
"""
def merge_sorted(arrays):
    n = len(arrays)
    if n < 2:
        return [] if n == 0 else arrays[0]

    q = []
    curr_idx = [0] * n
    for i in range(n):
        q.append((arrays[i][0], i))
        curr_idx[i] += 1
    heapify(q)

    res = []
    while q:
        p = heappop(q)
        res.append(p[0])
        arr_idx = p[1]
        pos = curr_idx[arr_idx]
        if pos < len(arrays[arr_idx]):
            heappush(q, (arrays[arr_idx][pos], arr_idx))
            curr_idx[arr_idx] += 1

    return res


#a = [1, 3, 5]
#b = [2, 4, 6]
#print merge_sorted([a, b])

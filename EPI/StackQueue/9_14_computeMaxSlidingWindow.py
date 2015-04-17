import os
import math
import imp
from collections import deque

from stack import Stack

"""
    ============================================================================================
    Given an array and an integer k, find the maximum for each and every contiguous subarray of
    size k.

    Example:

         Window position           Max
         ---------------          -----

    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    ============================================================================================
"""
def max_sliding_window(a, w):
    n = len(a)

    if n <= w:
        return max(a)

    res = [0] * (n - w + 1)
    q = deque()
    for i in range(0, w):
        while len(q) and a[i] >= a[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(w, n):
        res[i - w] = q[0]
        while len(q) and a[i] >= a[q[-1]]:
            q.pop()

        while len(q) and q[0] <= i - w:
            q.popleft()

        q.append(i)

    res[n - w] = q[0]
    res = [a[i] for i in res]
    return res


a = [1.3, 0, 2.5, 3.7, 0, 1.4, 2.6, 0, 2.2, 1.7, 0, 0, 0, 0, 1.7]
print max_sliding_window(a, 3)





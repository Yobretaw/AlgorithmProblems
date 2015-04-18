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

        # pop all elements that are smaller than the current element
        while len(q) and a[i] >= a[q[-1]]:
            q.pop()

        # pop all element whose index is smaller than the left bound of current window
        while len(q) and q[0] <= i - w:
            q.popleft()

        q.append(i)

    res[n - w] = q[0]
    res = [a[i] for i in res]
    return res



"""
    Similar to above problem, but now the function should return an array a where a[i] is
    the maximum value over the window length which ends at i.

    arr = [2.5, 3.7, 3.7, 3.7, 2.6, 2.6, 2.6, 2.2, 2.2, 1.7, 0, 0, 1.7], window_len = 3
    
    =>  [1.3, 1.3, 2.5, 3.7, 3.7, 3.7, 3.7, 2.6, 2.6, 2.6, 2.2, 2.2, 1.7, 0, 1.7]
"""
def max_sliding_window2(a, w):
    n = len(a)

    if n <= w:
        return max(a)

    res = []

    q = deque()
    for i in range(0, w + 1):
        while len(q) and a[i] >= a[q[-1]]:
            q.pop()
        q.append(i)
        res.append(a[q[0]])

    for i in range(w + 1, n):
        # pop all elements that are smaller than the current element
        while len(q) and a[i] >= a[q[-1]]:
            q.pop()

        # pop all element whose index is smaller than the left bound of current window
        while len(q) and q[0] <= i - w - 1:
            q.popleft()

        q.append(i)
        res.append(a[q[0]])

    return res

a = [1.3, 0, 2.5, 3.7, 0, 1.4, 2.6, 0, 2.2, 1.7, 0, 0, 0, 0, 1.7]
print max_sliding_window(a, 3)
print max_sliding_window2(a, 3)

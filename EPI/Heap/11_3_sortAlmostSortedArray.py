import sys
import os
import math
import imp
from heapq import *

"""
    Write a function that takes as input a very long sequence of numbers. Each
    number is at most k away from its correctly sorted position. For example,
    no number in the sequence [3, -1, 2, 6, 4, 5, 8] is more than 2 positions
    away from its final sorted position.

    Design an algorithm that outputs the numbers in the correct order.

    ===============================

    Time complexity: O(nlogk)
    Space complexity: O(k)
"""
def sort_k_sorted_array(arr, k):
    n = len(arr)
    if n < 2:
        return arr

    h = arr[:k]
    res = []
    for i in range(k, n):
        heappush(h, arr[i])
        heapify(h)
        res.append(heappop(h))

    while h:
        res.append(heappop(h))

    return res

#arr = [3, -1, 2, 6, 4, 5, 8]
#print sort_k_sorted_array(arr, 2)

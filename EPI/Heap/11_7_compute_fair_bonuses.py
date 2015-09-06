import sys
import os
import math
import imp
import random
from heapq import *

"""
    Same as the candy problem in Leetcode: https://leetcode.com/problems/candy/
"""
def compute_fair_bonus(arr):
    n = len(arr)
    if n < 2:
        return n

    counts = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            counts[i] = counts[i - 1] + 1

    for i in reversed(range(0, n - 1)):
        if arr[i] > arr[i + 1] and counts[i] <= counts[i + 1]:
            counts[i] = counts[i + 1] + 1

    return sum(counts)

#l = [1, 2, 3, 3, 5, 3, 2, 5]    # 1 + 2 + 3 + 1 + 3 + 2 + 1 + 2 = 15
#print compute_fair_bonus(l)

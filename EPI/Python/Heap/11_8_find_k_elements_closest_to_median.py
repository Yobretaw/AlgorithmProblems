import sys
import os
import math
import imp
import random
import functools
from heapq import *

select = imp.load_source('quick_select', '../Util/quick_select.py').select

"""
    Suppose you have an array and you want to find the k items in the array which
    are closest to the median. For example, for the array

                    <7, 14, 10, 12, 2, 11, 29, 3, 4>

    , if k = 5, then the median is 10 and the result is <7, 14, 10, 12, 11>

    Design an algorithm to compute the k elements closest to the median of an array.

    =====================================

    Use selection algorithm which reorders the array so that the k smallest difference 
    between median and each elements in array appear at the beginning of the diff
    array
    
    Time: O(n)
    Space: O(n)
"""
@functools.total_ordering
class FirstTuple(tuple):
    def __eq__(self, other):
        return self[0] == other[0]
    def __lt__(self, other):
        return self[0] < other[0]

def compute_k_closest_median(arr, k):
    n = len(arr)
    if n < 2 or not k:
        return [] if not n and not k else list(arr)

    median = find_median(arr)
    diff = [FirstTuple((math.fabs(v - median), v - median)) for v in arr]
    select(diff, k)
    return [int(v[1] + median) for v in diff[:k]]

def find_median(arr):
    n = len(arr)
    return select(list(arr), n / 2) if n % 2 == 1 else \
            float(select(list(arr), n / 2) + select(list(arr), n / 2 + 1)) / 2

l = [7, 14, 10, 12, 2, 11, 29, 3, 4]
for i in range(1, len(l)):
    print compute_k_closest_median(l, i)

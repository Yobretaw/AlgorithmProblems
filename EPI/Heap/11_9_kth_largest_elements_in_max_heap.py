import sys
import os
import math
import imp
import random
import functools
from heapq import *

"""
    Design an algorithm for determining whether the k-th largest element in a
    max-heap is smaller than, equal to, or larger than a given value. Return
    -1, 0, 1 these three cases respectively
"""
def kth_largest_in_heap(arr, k, v):
    """
        Return
           -1 if the kth largest in arr is less than v
            0 if the kth largest in arr is equal to v
            1 if the kth largest in arr is larger than v
    """
    larger = [0]
    equal = [0]
    kth_largest_in_heap_help(arr, k, 0, v, larger, equal)
    return 1 if larger[0] >= k else (0 if larger[0] + equal[0] >= k else -1)

def kth_largest_in_heap_help(arr, k, i, v, larger, equal):
    # Note we can't stop when larger[0] + equal[0] >= k as there might still be
    # values that are larger than x in other branches of the heap
    if i >= len(arr) or larger[0] >= k or arr[i] < v:
        return
    elif arr[i] == v:
        equal[0] += 1
    else:
        larger[0] += 1

    kth_largest_in_heap_help(arr, k, 2 * i + 1, v, larger, equal)
    kth_largest_in_heap_help(arr, k, 2 * i + 2, v, larger, equal)

#l = random.sample([-i for i in range(1000)], 1000)
#heapify(l)
#l = [-i for i in l]
#print kth_largest_in_heap(l, 100, 899)
#print kth_largest_in_heap(l, 100, 900)
#print kth_largest_in_heap(l, 100, 901)

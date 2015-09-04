import sys
import os
import math
import imp
from heapq import *

merge_sorted = imp.load_source('Merge', './11_1_mergeSortedFiles.py').merge_sorted

"""
    An array is said to be k-increasing-decreasing if elements repeatedly
    increase up to a certain index after which they decrease, then again
    increase. The lenght of one increasing-decreasing cycle is k.

    Design an efficient algorithm for sorting a k-increasing-decreasing array

    =================================
"""
def sort_inc_dec_array(arr):
    n = len(arr)
    if n < 2:
        return arr

    arrs = []
    incr = [arr[0]]
    decr = []
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            incr.append(arr[i])
            if decr:
                arrs.append(decr[::-1])
                decr = []
        else:
            decr.append(arr[i])
            if incr:
                arrs.append(incr)
                incr = []

    return merge_sorted(arrs)

arr = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
print sort_inc_dec_array(arr)

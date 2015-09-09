import sys
import os
import math
import imp
import random
import functools

"""
    Design an efficient algorithm that takes a sorted array of distinct integers,
    and returns an index i such that the element at index i equals i. 
"""
def search_for_equal_index(arr):
    n = len(arr)
    if n < 2:
        return -1 if not n or arr[0] != 0 else 0

    l, r = 0, n
    while l < r:
        mid = l + (r - l) / 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            r = mid
        else:
            l = mid + 1
    return -1


#arr = [-2, 0, 2, 3, 6, 7, 9]
#print search_for_equal_index(arr)

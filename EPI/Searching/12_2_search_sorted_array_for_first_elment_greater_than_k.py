import sys
import os
import math
import imp
import random
import functools

"""
    Design an efficient algorithm that takes a sorted array and a key, and finds
    the index of the first occurence of an element greater than that key.
"""
def find_first_occurence_greater_than_key(arr, k):
    n = len(arr)
    if n < 2:
        return -1 if not n or arr[0] <= k else 0

    l, r = 0, n
    while l < r:
        mid = l + (r - l ) / 2
        if arr[mid] <= k:
            if mid == n - 1 or arr[mid + 1] > k:
                return -1 if mid == n - 1 else mid + 1
            else:
                l = mid + 1
        else:
            if mid == 0:
                return 0
            else:
                r = mid
    return -1

#arr = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
#print find_first_occurence_greater_than_key(arr, -15)
#print find_first_occurence_greater_than_key(arr, -14)
#print find_first_occurence_greater_than_key(arr, -10)
#print find_first_occurence_greater_than_key(arr, 0)
#print find_first_occurence_greater_than_key(arr, 2)
#print find_first_occurence_greater_than_key(arr, 108)

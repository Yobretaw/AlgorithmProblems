import sys
import os
import math
import imp
import random
import functools

"""
    Write a method that takes a sorted array and a key and returns the index of
    the first occurence of that key in the array.
"""
def find_first_occurence(arr, k):
    n = len(arr)
    if n < 2:
        return -1 if not arr or arr[0] != k else 0

    l, r = 0, n
    while l < r:
        mid = l + (r - l ) / 2
        if arr[mid] == k:
            if mid == 0 or arr[mid - 1] != k:
                return mid
            else:
                r = mid
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid
    return -1

#arr = [1, 1, 1, 1, 1, 1, 1, 1]
#print find_first_occurence(arr, 1)

#arr = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
#print find_first_occurence(arr, -14)
#print find_first_occurence(arr, 108)
#print find_first_occurence(arr, 243)
#print find_first_occurence(arr, 285)
#print find_first_occurence(arr, 401)

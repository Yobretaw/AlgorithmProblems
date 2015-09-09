import sys
import os
import math
import imp
import random

"""
    An array is said to be cyclically sorted if it is possible to cyclically
    shifts its entries so that it become sorted. For example, the array bellow
    becomes sorted after being shiftted to the left by 4 positions.

    Design an O(logn) algorithm for finding the position of the smallest element
    in a cyclically sorted array. Assume all elements are distinct.
"""
def find_smallest_in_cyclically_sorted_array(arr):
    n = len(arr)
    if n < 2:
        return None if not n else 0

    l, r = 0, n
    while l < r:
        mid = l + (r - l) / 2
        if (mid == 0 and arr[mid] < arr[mid + 1]) or \
                (mid == n - 1 and arr[mid] < arr[0]) or \
                arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
                    return mid
        elif arr[mid] > arr[r - 1]:
            l = mid + 1
        else:
            r = mid
    return -1

#l = [5, 6, 7, 8, 9, 1, 2, 3, 4]
#l = [5, 6, 7, 8, 9]
#l = [5, 6, 7, 8, 9, 1]
#l = [6, 1, 2, 3, 4, 5]
#print find_smallest_in_cyclically_sorted_array(l)

import sys
import os
import math
import random

"""
    Design an algorithm for computing the k-th largest element in an array. Assume
    entries are distinct.

    ===========

    Use quick select
"""
def find_kth_largest_element(arr, k):
    return _select(arr, 0, len(arr) - 1, k - 1)

def _select(arr, left, right, k):
    while True:
        pivot_index = random.randint(left, right)
        pivot_new_index = partition(arr, left, right, pivot_index)
        pivot_dist = pivot_new_index - left
        if pivot_dist == k:
            return arr[pivot_new_index]
        elif pivot_dist > k:
            right = pivot_new_index - 1
        else:
            left = pivot_new_index + 1
            k -= pivot_dist + 1

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    stored_index = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[stored_index] = arr[stored_index], arr[i]
            stored_index += 1
    arr[right], arr[stored_index] = arr[stored_index], arr[right]
    return stored_index

#v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
#print([find_kth_largest_element(v, i) for i in range(1, len(v) + 1)])


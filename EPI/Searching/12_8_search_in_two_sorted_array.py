import sys
import os
import math
import imp
import random

"""
    You are given two given sorted arrays and a positive integer k. Design an
    algorithm for computing the k-th smallest element in array consisting of
    the elements of the initial two arrays arranged in sorted order. Array
    elements may be duplicated within and across the input arrays.
"""
def find_kth_largest_element(a, b, k):
    return find_kth_largest_element_help(a, 0, len(a), b, 0, len(b), k)

def find_kth_largest_element_help(a, i, alen, b, j, blen, k):
    #print i, alen, j, blen, k
    if alen <= 0 or blen <= 0:
        return a[i + k - 1] if blen <= 0 else b[j + k - 1]

    if k == 1:
        return min(a[i], b[j])

    mid_a = a[i + alen / 2]
    mid_b = b[j + blen / 2]
    if alen / 2 + blen / 2 + 1 < k:
        if mid_a > mid_b:
            return find_kth_largest_element_help(a, i, alen, b, j + (blen / 2 + 1), blen - (blen / 2 + 1), k - (blen / 2 + 1))
        else:
            return find_kth_largest_element_help(a, i + (alen / 2 + 1), alen - (alen / 2 + 1), b, j, blen, k - (alen / 2 + 1))
    else:
        if mid_a > mid_b:
            return find_kth_largest_element_help(a, i, alen / 2, b, j, blen, k)
        else:
            return find_kth_largest_element_help(a, i, alen, b, j, blen / 2, k)

#a = [1, 3, 5, 7, 9]
#b = [2, 4, 6, 8, 10]
#for i in range(1, len(a) + len(b) + 1):
#    print find_kth_largest_element(a, b, i)

#print find_kth_largest_element(a, b, 3)

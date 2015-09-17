import sys
import os
import math
import random

"""
    You are given an array of n integers, each between 0 and n - 1, inclusive.
    Exactly one element appears twice, implying that extacly one number between
    0 and n - 1 is missing from the array. How would you compute the duplicate
    and missing nubmers?

    =============

    Let t be the element that appears twice, and m be the missing number. If m
    and t differ in the k-th bit, we compute the XOR of the nubmers from 0 to
    n - 1 in which the k-th bit is 1, and the entries in the array in which
    the k-th bit is 1. Let this XOR be h, h must be one of m or t. We can then
    make another pass through A to determine if h is th duplicate or the missing
    element.
"""
def find_duplicate_and_missing_elements(arr):
    n = len(arr)

    miss_XOR_dup = 0
    for i, v in enumerate(arr):
        miss_XOR_dup ^= i ^ arr[i]

    differ_bit = miss_XOR_dup & ~(miss_XOR_dup - 1)
    miss_or_dup = 0
    for i, v in enumerate(arr):
        if i & differ_bit:
            miss_or_dup ^= i
        if arr[i] & differ_bit:
            miss_or_dup ^= arr[i]

    for v in arr:
        if v == miss_or_dup:
            return miss_or_dup, miss_or_dup ^ miss_XOR_dup
    
    return miss_or_dup ^ miss_XOR_dup, miss_or_dup

a = [5, 3, 0, 3, 1, 2]
print find_duplicate_and_missing_elements(a)


import sys
import os
import math


"""
    Write a function that takes as input an array A of n distinct integers and
    prints all permutations of A. No permutation appear more than once. Your
    function should use O(n) space.
"""
def enumerate_permutation(arr):
    if not arr:
        return

    enumerate_permutation_help(arr, 0)

def enumerate_permutation_help(arr, idx):
    if idx == len(arr):
        print arr
        return

    for i in range(idx, len(arr)):
        arr[i], arr[idx] = arr[idx], arr[i]
        enumerate_permutation_help(arr, idx + 1)
        arr[i], arr[idx] = arr[idx], arr[i]


"""
    Variant 16.4.1

    Solve the same problem when the input array may have duplicates. You should
    not repeat any permutation.
"""
def enumerate_permutation_dup(arr):
    if not arr:
        return

    arr.sort()
    enumerate_permutation_dup_help(arr, 0)

def enumerate_permutation_dup_help(arr, idx):
    if idx == len(arr):
        print arr
        return

    seen = set()
    for i in range(idx, len(arr)):
        if arr[i] in seen:
            continue

        seen.add(arr[i])

        arr[i], arr[idx] = arr[idx], arr[i]
        enumerate_permutation_dup_help(arr, idx + 1)
        arr[i], arr[idx] = arr[idx], arr[i]


if __name__ == '__main__':
    #enumerate_permutation([i for i in range(0, 4)])
    #enumerate_permutation_dup([2, 2, 3, 0])

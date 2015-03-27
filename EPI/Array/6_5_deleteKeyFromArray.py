import sys
import os
import re
import math


"""
    ============================================================================================
    Implement a function which takes as input of an array A of integers and an integer k, and
    update A so that all occurences of k have been removed from A and remaining elements have
    been shifted to the left to fill the emptied indices. The function should return the number
    of remaining elements in the array.
    ============================================================================================
"""
def remove(A, k):
    curr = 0

    for val in A:
        if val == k:
            continue

        A[curr] = val
        curr += 1

    return curr


print remove([5, 3, 7, 11, 2, 3, 13, 5, 7], 2)
print remove([5, 3, 7, 11, 2, 3, 13, 5, 7], 3)
print remove([5, 3, 7, 11, 2, 3, 13, 5, 7], 5)
print remove([5, 3, 7, 11, 2, 3, 13, 5, 7], 11)


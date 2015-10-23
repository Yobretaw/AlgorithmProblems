import sys
import math
import itertools


"""
    Write a function which takes as input two sorted arrays of integers, and
    updates the first to the combined entries of the two arrays in sorted
    order. Assume the first array has enough empty entries at its end to hold
    the result.

    Empty entries will be filled with 'None'.
"""
def mergesort_inplace(A, B):
    m, n = len(A), len(B)

    if not m or A[0] == None:
        A[:n] = B
        return

    if not n:
        return

    # first count the # non-empty entries in A
    count_a = 0
    for i, v in enumerate(A):
        if v == None:
            break
        count_a += 1

    # then move all elements of A to the end of A
    A[-count_a:] = A[:count_a]
    A[:count_a] = [None] * count_a

    # merge two arrays
    i, j = m - count_a, 0
    pos = 0
    while i < m or j < n:
        a = A[i] if i < m else None
        b = B[j] if j < n else None

        if a == None:
            A[pos] = b
            j += 1
        elif b == None:
            A[pos] = a
            i += 1
        elif a < b:
            A[pos] = a
            i += 1
        else:
            A[pos] = b
            j += 1
        pos += 1
    
    # in case of 'count_a + n < m', clear rest elements in A
    A[pos:] = [None] * (m - pos)
    return


A = [5, 13, 17, None, None, None, None, None]
B = [3, 7, 11, 19]
mergesort_inplace(A, B)
print A

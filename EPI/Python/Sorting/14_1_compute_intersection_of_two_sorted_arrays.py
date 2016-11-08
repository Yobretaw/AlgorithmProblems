import sys
import math
import itertools


"""
    Given two sorted arrays, return a new array containing elements common to
    the two arrays. You can assume that the input arrays are free of dupilcates.
    The new array should be free of dupilcates.
"""
def merge_sorted_arrays(A, B):
    if not A or not B:
        return A if not B else B

    m, n = len(A), len(B)
    res = [None] * (m + n)
    count = 0
    i = j = 0

    while i < m or j < n:
        a = A[i] if i < m else None
        b = B[j] if j < n else None

        if b == None or (a != None and a < b):
            if a != (res[count - 1] if count > 0 else None):
                res[count] = a
                count += 1
            i += 1
        else:
            if b != (res[count] if count > 0 else None):
                res[count] = b
                count += 1
            j += 1

    return res[:count]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [2, 3, 5, 6, 8, 9, 10, 11, 13]
    print merge_sorted_arrays(A, B)


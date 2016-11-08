import sys
import os
import math
from heapq import *
from BST import Node


"""
    Let A, B and C be sorted arrays of integers. Define distance(i, j, k) = 
    max(|A[i] - B[j]|, |A[i] - C[k]|, |B[j] - C[k]|).

    Design an algorithm that takes three sorted arrays A, B and C and returns
    a triple (i, j, k) such that distance(i, j, k) is minimum. You algorithm
    should run in O(len(A) + len(B) + Len(C)) time.
"""
def compute_closest_entries(A, B, C):
    i = j = k = 0
    min_dist = sys.maxint
    while i < len(A) and j < len(B) and k < len(C):
        a, b, c = A[i], B[j], C[k]

        min_dist = min(min_dist, compute_distance(a, b, c))
        min_val = min(a, b, c)

        if min_val == a:
            i += 1
        elif min_val == b:
            j += 1
        else:
            k += 1

    return min_dist


def compute_distance(a, b, c):
    return max(
        abs(a - b),
        abs(a - c),
        abs(b - c)
    )


if __name__ == '__main__':
    A = [1, 3, 9, 14, 22]
    B = [5, 7, 12, 18, 30]
    C = [16, 26, 33, 41]
    print compute_closest_entries(A, B, C)

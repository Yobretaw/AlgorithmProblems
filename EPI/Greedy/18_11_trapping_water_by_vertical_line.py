import sys
import math


"""
    Define the water trapped by entries i and j in an integer array A to be
    |j - i| * min(A[i], A[j]). Write a function wihch takes as input A and
    returns the pair of entries that trap the maximum amount of water.

    ----

    We focus on an interval [i, j] which we know must contain any solution not
    considered so far. Initially, i = 0 and j = n - 1. We record the water
    trapped by A[0] and A[n - 1] in r. Suppose A[0] < A[n - 1]. Then for any
    x in between 0 and n - 1, the water trapped by A[0] and A[x] is less than
    r, so we never need to consider A[0] again. The same applies to the case
    where A[0] > A[n - 1]. In this way, we iteratively eliminiate at least one
    line at a time, spending O(1) time per iteration. The time complexity is
    O(n).
"""
def trapping_water_by_line(A):
    n = len(A)
    if n < 2:
        return (-1, -1)

    i, j = 0, n - 1
    res = 0
    while i < j:
        res = max((j - i) * min(A[i], A[j]), res)

        if A[i] < A[j]:
            i += 1
        elif A[i] > A[j]:
            j -= 1
        else:
            i += 1
            j -= 1

    return res


if __name__ == '__main__':
    pass

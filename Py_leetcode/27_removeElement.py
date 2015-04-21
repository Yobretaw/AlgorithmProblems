import sys
import math
import imp

"""
    Given an array and a value, remove all instances of that value in place and return the new length.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
def remove_element(A, k):
        if not A:
            return 0

        p = 0
        for i in range(0, len(A)):
            if A[i] != k:
                A[p] = A[i]
                p += 1

        return p

#A = [1, 1, 2, 3, 4, 2, 1]
#print remove_element(A, 2)

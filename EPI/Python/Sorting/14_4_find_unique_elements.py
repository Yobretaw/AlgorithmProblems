import sys
import math
import itertools
import string
from collections import Counter


"""
    Design an efficient algorithm to remove all the duplicates from an array.
"""
def remove_duplicates(A):
    n = len(A)
    if n < 2:
        return

    seen = set([A[0]])
    write_idx = 1
    curr_idx = 1
    while curr_idx < n:
        if A[curr_idx] in seen:
            curr_idx += 1
        else:
            A[write_idx] = A[curr_idx]
            write_idx += 1
            seen.add(A[curr_idx])

    A[:] = A[:write_idx]
    return

def remove_duplicates2(A):
    n = len(A)
    if n < 2:
        return

    A.sort()
    write_idx = 1
    curr_idx = 1
    while curr_idx < n:
        if A[curr_idx] == A[curr_idx - 1]:
            curr_idx += 1
        else:
            A[write_idx] = A[curr_idx]
            curr_idx += 1
            write_idx += 1

    A[:] = A[:write_idx]
    return

if __name__ == '__main__':
    A = [1, 4, 2, 3, 5, 6, 4, 3, 1, 9, 0]
    remove_duplicates(A)
    print A

    A = [1, 4, 2, 3, 5, 6, 4, 3, 1, 9, 0]
    remove_duplicates2(A)
    print A

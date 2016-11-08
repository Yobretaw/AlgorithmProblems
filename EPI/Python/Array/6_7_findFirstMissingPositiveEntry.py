import sys
import os
import re
import math

"""
    ============================================================================================
    Let A be an array of length n. Design an algorithm to find the smallest positive integer
    which is not present in A. You don't need to preserve the contents of A. For example, if A = 
    [3, 5, 4, -1, 5, 1, -1], the smallest positive integer not present in A is 2.
    ============================================================================================
"""
def find_smallest_not_present(A):
    """
        Brute force: sort A first and traverse the array
    """
    n = len(A)

    if n == 0:
        return 1

    A.sort()
    curr = 1

    for i in range(0, n):
        if A[i] < curr:
            continue
        if A[i] != curr:
            return curr
        else:
            curr += 1

    return curr

def find_smallest_not_present2(A):
    """
        Use hashtable
    """
    n = len(A)

    if n == 0:
        return 1

    m = {}
    for val in A:
        m[val] = 1

    i = 1
    while True:
        if m.get(i) == None:
            return i
        i += 1

    return i

def find_smallest_not_present3(A):
    """
        Use A itself as a hashtable

        The problem statement gives us a hint which we can use to  reduce the space complexity.
        Instead of using an external hash table to store the set of positive integers, we can
        use A itself. Specifically, if A contains k between 1 and n, we set A[k - 1] to k.
        (We use k - 1 because we need to use all n entries, including the entry at index 0, which
        will be used to store the presence of 1). Note that we need to save the presence of
        existing entry in A[k - 1] if it's between 1 and n. Because A contains n entries, the
        smallest positive number that is missing in A cannot be greater that n + 1.

        Then we make a pass through A looking for the first index i such that A[i] != i + 1.
    """
    n = len(A)

    if n == 0:
        return 1

    i = 0
    while i < n:
        if A[i] > 0 and A[i] <= n and A[A[i] - 1] != A[i]:
            # DONT'T USE THIS EXPRESSION!!!!: A[i], A[A[i] - 1] = A[A[i] - 1], A[i]
            a = A[A[i] - 1]
            b = A[i]

            A[A[i] - 1] = b
            A[i] = a
        else:
            i += 1

    for i in range(0, n):
        if A[i] != i + 1:
            return i + 1

    return n + 1


l = [3, 5, 3, -1, 5, 1, 2, -1]
print find_smallest_not_present(l)
print find_smallest_not_present2(l)
print find_smallest_not_present3(l)


import sys
import math

"""
    Design an algorithm that takes as abs-sorted array A and a number K, and
    returns a pair of indices of elements in A that sum up to K.

    An abs-sorted array is an array of numbers in which |A[i]| <= |A[j]| whenever
    i < j.
"""
# This algorithm takes O(n) time and O(n) space.
def search_pair_sum(A, k):
    n = len(A)
    if n < 2:
        return (-1, -1)

    m = { val: i for i, val in enumerate(A) }

    for i, v in enumerate(A):
        if k - v in m and m[k - v] != i:
            return (min(i, m[k-v]), max(i, m[k-v]))

    return (-1, -1)

"""
    If the array is sorted in conventional sense, then there is an algorithm that
    solves this problem in O(n) time and O(1) space.

    In this instance, we consider three cases: 

    (1) Both the numbers in the pair are negative. 
    (2) Both the numbers in the pair are positive. 
    (3) One is negative and the other is positive. 

    For Cases (1) and (2), we can run the above algorithm separately by just
    limiting ourselves to either positive or negative numbers. For Case (3),
    we can use the same approach where we have on index for positive numbers,
    one index for negative numbers, and they both start from the highest possible
    index and then go down.
"""
def search_pair_sum2(A, k):
    n = len(A)
    if n < 2:
        return (-1, -1)

    # first we handle the case where both numbers in the pair are positive
    if k > 0:
        i, j = 0, n - 1
        while i < j:
            while i < j and A[i] < 0:
                i += 1
            while i < j and A[j] < 0:
                j -= 1

            if i >= j:
                break

            s = A[i] + A[j]
            if s == k:
                return (i, j)
            elif s < k:
                i += 1
            else:
                j -= 1

    # next we handle the case where both numbers in the pair are negative
    if k < 0:
        i, j = 0, n - 1
        while i < j:
            while i < j and A[i] > 0:
                i += 1
            while i < j and A[j] > 0:
                j -= 1

            if i >= j:
                break

            s = A[i] + A[j]
            if s == k:
                return (i, j)
            elif s < k:
                j -= 1
            else:
                i += 1

    # next we handle the case where one is negative and one is positive
    i, j = n - 1, n - 1
    while i >= 0 and j >= 0:
        while i >= 0 and A[i] < 0:
            i -= 1
        while j >= 0 and A[j] > 0:
            j -= 1

        if i < 0 or j < 0:
            break

        s = A[i] + A[j]
        if s == k:
            return (min(i, j), max(i, j))
        elif s > k:
            i -= 1
        else:
            j -= 1

    return (-1, -1)

if __name__ == '__main__':
    A = [-49, 75, 103, -147, 164, -197, -238, 314, 348, -422]
    k = 167
    print search_pair_sum(A, k)
    print search_pair_sum2(A, k)

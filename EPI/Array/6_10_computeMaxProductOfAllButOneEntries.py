import sys
import os
import re
import math

"""
    ============================================================================================
    Given an array A of length n whose entries are integers, compute the largest product that can
    be made using n - 1 entries in A. You cannot use an entry more than once. Array entries may
    be positive, negative, or 0. Your algorithm cannot use the division operator, explicitly or
    implicitly.
    ============================================================================================
"""
def computeMaxProduct(A):
    n = len(A)

    if n < 2:
        return 0

    neg_count = 0
    zero_count = 0
    max_neg = -sys.maxint
    min_pos = sys.maxint
    for i in range(0, n):
        if A[i] < 0:
            neg_count += 1
            max_neg = A[i] if A[i] > max_neg else max_neg
        elif A[i] == 0:
            zero_count += 1
        else:
            min_pos = A[i] if A[i] < min_pos else min_pos

    if zero_count > 1:
        return 0

    if not (neg_count & 0) and zero_count == 1:
        return 0

    product = 1
    
    if zero_count:
        for val in A:
            if not val:
                product *= val
    elif neg_count & 1:
        for val in A:
            if val != max_neg or max_neg == 0:
                product *= val
            elif val == max_neg:
                max_neg = 0
    else:
        for val in A:
            if val != min_pos or min_pos == 0:
                product *= val
            elif val == min_pos:
                min_pos = 0

    return product

def computeMaxProduct2(A):
    n = len(A)

    if n < 2:
        return 0

    L = [1] * n
    R = [1] * n

    for i in range(0, n):
        L[i] = A[0] if i == 0 else A[i] * L[i - 1]

    for i in reversed(range(0, n)):
        R[i] = A[i] if i == n - 1 else A[i] * R[i + 1]

    max_product = -sys.maxint
    for i in range(0, n):
        forward = L[i - 1] if i > 0 else 1
        backward = R[i + 1] if i + 1 < n else 1

        max_product = max(max_product, forward * backward)

    return max_product


l = [3, 2, 5, 4]
print computeMaxProduct(l)
print computeMaxProduct2(l)

l = [3, 2, -1, 4]
print computeMaxProduct(l)
print computeMaxProduct2(l)

l = [3, 2, -1, 4, -1, 6]
print computeMaxProduct(l)
print computeMaxProduct2(l)



"""
    Variant 6.10.1: Let A be as above. Compute an array B where B[i] is the product of
    all elements in A excpet A[i]. You cannot use division. Your time complexity should
    be O(n), and you can only use O(1) additional space.
"""
def computeArray(A):
    n = len(A)

    if n < 2:
        return []

    B = [0] * n
    for i in reversed(range(0, n)):
        B[i] = A[i] if i == n - 1 else A[i] * B[i + 1]

    for i in range(1, n):
        A[i] = A[i] * A[i - 1]

    for i in range(0, n):
        forward = A[i - 1] if i > 0 else 1
        backward = B[i + 1] if i + 1 < n else 1

        B[i] = forward * backward

    return B

l = [3, 2, 5, 4]
print computeArray(l)
l = [3, 2, -1, 4, -1, 6]
print computeArray(l)

"""
    Variant: 6.10.2: Let A be as above. Compute the maximum over the product of all triples
    of distinct elements of A.
"""
def computeMaxTripleProduct(A):
    n = len(A)

    if n < 3:
        return 0

    max_val = 0
    for val in A:
        max_val = val if val > max_val else max_val

    pos_max = 0
    pos_sec = 0
    neg_min = 0
    neg_sec = 0
    for val in A:
        if val > pos_max and val != max_val:
            pos_sec = pos_max
            pos_max = val
        elif val != pos_max and val != max_val and val > pos_sec:
            pos_sec = val
        elif val < neg_min:
            neg_sec = neg_min
            neg_min = val
        elif val != neg_min and val < neg_sec:
            neg_sec = val

    a = pos_max * pos_sec
    b = neg_min * neg_sec

    return max_val * (a if a > b else b)


l = [3, 2, 5, 4]
print computeMaxTripleProduct(l)
l = [3, 2, -1, 4, -1, 6]
print computeMaxTripleProduct(l)

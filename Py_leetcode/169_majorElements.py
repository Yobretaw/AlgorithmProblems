import sys
import math

"""
    Given an array of size n, find the majority element. The majority element is the element
    that appears more than floor(n/2) times.

    You may assume that the array is non-empty and the majority element always exist in the array.
"""
def major_elements(A):
    n = len(A)
    if n < 2:
        return A[0] if n else 0

    idx = 0
    max_idx = 0
    max_count = 1
    count = 1
    val = A[0]
    for i in range(1, n):
        if A[i] == val:
            max_idx = i
            count += 1
        else:
            count -= 1

        if count == 0:
            val = A[i]
            count = 1
    return A[max_idx]


#a = [1, 1, 3, 3, 3, 3, 4, 4 ,1, 1, 1]
#print major_elements(a)

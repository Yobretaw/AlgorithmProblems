import sys
import os
import re
import math

"""
    ============================================================================================
    Write a function that takes an array A of length n and an index i into A, and rearranges the
    elements such that all elements less than A[i] appear first, followed by elements equal to
    A[i], followed by elements greater than A[i]
    ============================================================================================

    Solution:

        Maintain four groups: bottom(elements less than pivot), middle(elements equals to pivot),
    unclassfied, and top(elements larger than pivot). These groups are stored in contiguous order
    in a. To make this partitioning run in O(1) space, we use variables 'smaller', 'equal', and
    'larger' to track these groups in the following way.

        - bottom: stored in subarray A[0, smaller - 1]
        - middle: stored in subarray A[smaller, equal - 1]
        - unclassfied: stored in subarray A[equal, larger - 1]
        - top: stored in subarray A[larger, n - 1]

    We explore elements of unclassfied in order, and classify the elements into one of 'bottom',
    'middle', and 'top' groups according to the relative order between the incoming unclassfied
    elements and pivot. Each interation decreases the size of unclassfied group by 1, and the 
    time spent within each interation is O(1), implying the time complexity if O(n)
"""
def rearrange(A, i):
    n = len(A)

    if n < 2:
        return

    smaller = 0
    equal = 0
    larger = n
    pivot = A[i]

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[equal], A[larger - 1] = A[larger - 1], A[equal]
            larger -= 1

l = [4, 2, 5, 3, 1, 5, 7, 4, 2, 4]
rearrange(l, 0)
print l



"""
    ===============================================================================================
    Varian 6.1.1 Assuming that keys take one of three values, reorder the array so that all objects
    with the same key appear together. The order of the subarray is not important. Use O(1) space
    and O(n) time.
    ===============================================================================================
"""
def rearrange1(A):
    pass



"""
    ===============================================================================================
    Varian 6.1.1 Assuming that keys take one of four values, reorder the array so that all objects
    with the same key appear together. The order of the subarray is not important. Use O(1) space
    and O(n) time.
    ===============================================================================================
"""
def rearrange2(A):
    pass


"""
    ===============================================================================================
    Given an array A of n objects with boolean-valued keys, reorder the array so that all objects
    that have the key false appear first. Use O(1) addition space and O(n) time.
    ===============================================================================================
"""
def rearrange3(A):
    pass


"""
    ===============================================================================================
    Given an array A of n objects with boolean-valued keys, reorder the array so that all objects
    that have the key false appear first. The relative ordering of objects with key true should 
    not change. Use O(1) addition space and O(n) time.
    ===============================================================================================
"""
def rearrange4(A):
    pass

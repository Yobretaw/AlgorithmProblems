import sys
import os
import re
import math

"""
    ==============================================================================================
    Write a function which takes as input a sorted array A and updates A so that all duplicates
    have been removed and the remaining elements have been shifted left to fill emptied indices.
    Return the number of valid elements in A.
    ==============================================================================================
"""
def remove_duplicates(A):
    n = len(A)
    
    if n < 2:
        return

    curr = 0
    for i in range(1, n):
        if A[curr] != A[i]:
            A[curr + 1] = A[i]
            curr += 1

    return curr


#l = [2, 3, 5, 5, 6, 11, 11, 11, 13]
#l = [1, 2, 3, 4]
#print remove_duplicates(l)
#print l




"""
    ==============================================================================================
    Variant 6.6.1: Write a function which takes as input a sorted array A of integers and a positive
    integer m, and updates A so that if x appears m times in A it appears exactly min(2, m) times
    in A. The update to A should be performed in one pass, and no additional storge may be used.
    ==============================================================================================
"""
def update_array(A, m):
    pass

#l = [2, 3, 5, 5, 6, 11, 11, 11, 13]
#update_array(l, 1)
#print l

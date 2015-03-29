import sys
import os
import re
import math
import random

"""
    ============================================================================================
    A permutation of an array A can be specified by an array P, where P[i] represents the location
    of the element at i in the permutation. A permutation can be applied to an array to reorder the
    array. For example, the permutation [2, 0, 1, 3] applied to [a, b, c, d] yields the array
    [b, c, a, d]. It simple to apply a permutation to a given array if additional storge is available
    to write the resulting array

    Given an array A of n elements and a permutation P, apply P to A using only constant additional
    storge. Use A itself to store the result.

    Essentially it's bucket sort.


    [2, 0, 1, 3]
    [a, b, c, d]

    ->

    [1, 0, 2, 3]
    [c, b, a, d]

    ->

    [0, 1, 2, 3]
    [b, c, a, d]
    ============================================================================================
"""
def permutate(A, P):
    n = len(A)

    if n < 2:
        return A

    for i in range(0, n):
        while i != P[i]:
            a = P[i]
            A[i], A[a] = A[a], A[i]
            P[i], P[a] = P[a], a

A = ['a', 'b', 'c', 'd']
P = [2, 0, 1, 3]
permutate(A, P)
print A


A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
P = [2, 6, 4, 5, 3, 7, 0, 8, 9, 1]

permutate(A, P)
print A

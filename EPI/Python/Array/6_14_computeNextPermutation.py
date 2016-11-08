import sys
import os
import re
import math
import random


"""
    ============================================================================================
    Given a permutation p, return the next permutation under dictionary ordering. If p is the last
    permutation, return the empty array. For example, if p = [1, 0, 3, 2], return [1, 2, 0, 3]
    ============================================================================================


    Solution: The general algorithm is as follows:
        
        1. Find k such that p[k] < p[k + 1] and entries after index k appear in decreasing order.
        2. Find the smallest p[l] such that p[l] > p[k] for l > k. Such l must exist since p[k] < p[k + 1]
        3. Swap p[l] and p[k](note that the sequence after index k remains in decreasing order)
        4. Reverse the sequence after index k to produce the next permutation
"""
def nextPermutation(p):
    p = list(p)
    n = len(p)
    
    if n < 2:
        return []

    k = n - 2
    while k >= 0 and p[k] >= p[k + 1]:
        k -= 1

    if k == -1:
        return []

    for i in reversed(range(k + 1, n)):
        if p[i] > p[k]:
            p[k], p[i] = p[i], p[k]
            break

    p[k + 1 : n] = reversed(p[k + 1 : n])
    return p


#p = [1, 0, 3, 2]
#nextPermutation(p)
#print p

#p = [6, 2, 1, 5, 4, 3, 0]
#nextPermutation(p)
#print p


"""
    Variant 6.14.1: Compute the k-th permutation under dictionary ordering, starting from the
    identity permutation(which is the first permutation in dictionary ordering: [1, 2, .. , n])
"""
def kPermutation(n, k):
    fac = [1] * n

    for i in range(1, n):
        fac[i] = i * fac[i - 1]

    digits = [0] * n
    result = [0] * n

    k -= 1

    # reversed CANTOR EXPANSION OF A NUMBER
    for i in range(0, n):
        curr_fac = k / fac[n - i - 1]
        idx = getNextDigit(digits, curr_fac)

        result[i] = idx             # 0-based sequence
        #result[i] = idx + 1        # 1-based sequence

        k %= fac[n - i - 1]

    return result

 # find i such that i is available and there are exactly
 # m digits smaller than i are available
 # 
 # i is available iff digits[i] = 0
def getNextDigit(digits, m):
    for i in range(0, len(digits)):
        if digits[i]:
            continue

        if m == 0:
            digits[i] = 1
            return i

        m -= 1

#n = 4
#for i in range(0, math.factorial(n)):
#    print kPermutation(n, i + 1)

"""
    Variant 6.14.2: Given a permutation p, return the permutation corresponding to the previous
    permutation of p under dictionary ordering.

    Solution: The general algorithm is as follows:
        
        1. Find k such that p[k] > p[k + 1] and entries after index k appear in increasing order.
        2. Find the largest p[l] such that p[l] < p[k] for l > k. Such l must exist since p[k] > p[k + 1]
        3. Swap p[l] and p[k](note that the sequence after index k remains in increasing order)
        4. Reverse the sequence after index k to produce the previous permutation
"""
def prevPermutation(p):
    p = list(p)
    n = len(p)

    if n < 2:
        return []

    idx = -1
    for i in reversed(range(1, n)):
        if p[i] < p[i - 1]:
            idx = i - 1
            break

    if idx == -1:
        return []

    for i in reversed(range(idx + 1, n)):
        if p[i] < p[idx]:
            p[i], p[idx] = p[idx], p[i]
            break

    p[idx + 1 : n] = reversed(p[idx + 1 : n])
    return p


#p = [6, 2, 1, 5, 4, 3, 0, 8]
#l = list(p)

#print l
#print prevPermutation(p)
#print nextPermutation(prevPermutation(p))

#p = [0, 1, 3, 4, 2]
#print p
#print nextPermutation(p)
#print prevPermutation(p)

n = 5
for i in range(1, math.factorial(n - 1)):
    l = kPermutation(n, i + 1)
    p = list(l)
    print nextPermutation(l) == kPermutation(n, i + 2)
    print prevPermutation(nextPermutation(l)) == p

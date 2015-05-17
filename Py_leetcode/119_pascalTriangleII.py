import sys
import os
import math
import imp
from collections import deque

"""
    Given an index k, return the kth row of the Pascal's triangle.

    For example, given k = 3,
    Return [1,3,3,1].

    Note:
    Could you optimize your algorithm to use only O(k) extra space?
"""
def generate(k):
    res = []
    for i in range(0, k + 1):
        tmp = list(res)
        for j in range(1, len(res)):
            res[j] = tmp[j - 1] + tmp[j]
        res += [1]
    return res

def generate2(k):
    res = []
    for i in range(0, k + 1):
        for j in reversed(range(1, len(res))):
            res[j] += res[j - 1]
        res += [1]
    return res

#for i in range(0, 10):
#    print generate(i)
#    print generate2(i)

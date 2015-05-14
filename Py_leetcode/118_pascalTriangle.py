import sys
import os
import math
import imp
from collections import deque

"""
    Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""
def generate(k):
    res = []
    for i in range(0, k):
        curr = list(res[-1]) if len(res) else []
        for i in range(1, len(curr)):
            curr[i] = res[-1][i - 1] + res[-1][i]
        res.append(curr + [1])
    return res


#for i in range(1, 10):
#    print generate(i)

import sys
import os
import math
import imp
import random
from heapq import *

"""
    Design an algorithm for computing the running median of a sequence
"""
def compute_median(next_num_func):
    l = [sys.maxint]
    s = [-sys.maxint]

    for a in next_num_func():
        max_small = -s[0]
        min_large = l[0]
        diff = len(l) - len(s)

        if a < max_small:
            heappush(s, -a)
        elif a > min_large:
            heappush(l, a)
        else:
            heappush(s, -a)

        if len(l) - len(s) > 1:
            heappush(s, -heappop(l))
        elif len(l) - len(s) < -1:
            heappush(l, -heappop(s))

    if (len(l) + len(s)) % 2 == 0:
        return (l[0] + -s[0]) / 2
    else:
        return l[0] if len(l) < len(s) else -s[0]


def next_num():
    nums = random.sample([i for i in range(1024)], 1024)
    for i in range(len(nums)):
        yield nums[i]

#print compute_median(next_num)

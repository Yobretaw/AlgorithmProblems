import sys
import math
from collections import defaultdict

"""
    Given a set of distinct numbers, find all subsets of this set.
"""
def subset(s):
    if not s or len(s) == 1:
        return s if len(s) == 1 else []

    res = []
    subset_help(s, 0, [], res)
    return res


def subset_help(s, idx, curr, res):
    n = len(s)

    if idx == n:
        res.append(list(curr))
        return

    curr.append(idx)
    subset_help(s, idx + 1, curr, res)
    curr.pop()
    subset_help(s, idx + 1, curr, res)


"""
    Subset without recursion
"""
def subset_iterative(s):
    if not s or len(s) == 1:
        return s if len(s) == 1 else []

    res = [[]]
    for num in s:
        new_res = []
        for curr in res:
            new_set = list(curr)
            new_set.append(num)
            new_res.append(new_set)
        res.extend(new_res)
    return res



#s = [1, 2, 3, 4, 5]
#print len(subset(list(s)))
#print '-' * 100
#print len(subset_iterative(list(s)))

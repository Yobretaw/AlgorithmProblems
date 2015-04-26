import sys
import math
from collections import defaultdict

"""
    Given a set of numbers, find all distinct subsets of this set.

    For example, if s = [1, 2, 2],
    
    return:
        [],
        [1],
        [2],
        [1, 2]
        [2, 2]
        [1, 2, 2]
"""
def subset_unique(s):
    if not s or len(s) == 1:
        return [s] if len(s) == 1 else []

    res = []
    subset_unique_help(s, 0, [], res)
    return res

def subset_unique_help(s, idx, curr, res):
    n = len(s)
    if idx == n:
        res.append(list(curr))
        return

    next_idx = idx
    while next_idx < n and s[next_idx] == s[idx]:
        next_idx += 1

    # not include s[idx]
    subset_unique_help(s, next_idx, curr, res)

    for i in range(idx, next_idx):
        curr.append(s[i])
        subset_unique_help(s, next_idx, curr, res)

    for i in range(idx, next_idx):
        curr.pop()


"""
    find unique subset without using recursion.
"""
def subset_unique_iterative(s):
    n = len(s)
    if n < 2:
        return [s] if n == 1 else []

    res = [[]]
    for num in s:
        new_res = []
        for curr in res:
            new_curr = list(curr)
            new_curr.append(num)
            new_res.append(new_curr)
            
            if curr and curr[-1] == num:
                break
        res.extend(new_res)
    return res

#s = [1, 2, 2, 3, 3]
#print subset_unique_iterative(s)

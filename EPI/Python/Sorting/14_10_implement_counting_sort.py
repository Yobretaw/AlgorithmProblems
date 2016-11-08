import sys
import math
from collections import defaultdict


"""
    You are given an array of objects. Each object has a field that is to be
    treated as a key. Rearrange the elements of the array so that objects with
    equal keys appear together. The order in which distinct keys appear is not
    important.
"""
class MyObj:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return str(self.key) + ': ' + str(self.val)


def counting_sort(A):
    # assume A is an array of integers
    keyCount = defaultdict(list)
    for v in A:
        keyCount[v.key].append(v)

    res = []
    for k in keyCount.keys():
        res.extend(keyCount[k])
    return res

if __name__ == '__main__':
    vals = ['b', 'a', 'c', 'b', 'd', 'a', 'b', 'd']
    vals = [MyObj(v, v) for v in vals]
    print counting_sort(vals)

import sys
import math
from collections import defaultdict

"""
    Given a collection of numbers, return all possible permutations.

    For example,
    [1,2,3] have the following permutations:
    [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""
def permutations(num):
    if not num or len(num) == 1:
        return [num] if len(num) == 1 else []

    res = []
    permutations_help(num, 0, [], res)
    return res

def permutations_help(num, idx, curr, res):
    n = len(num)
    if idx == n - 1:
        res.append(list(num))
        return

    for i in range(idx, n):
        num[i], num[idx] = num[idx], num[i]
        permutations_help(num, idx + 1, curr, res)
        num[i], num[idx] = num[idx], num[i]


def permute_map_reduce(self, num):
    def generate(i):
        num[0], num[i] = num[i], num[0]
        return [[num[0]] + each for each in self.permute(num[1:])]
    return reduce(lambda x, y: x + y, map(generate, range(len(num))), []) or [[]]


def permute_iterative(self, num):
    if not num:
        return num

    res = [[num[0]]]
    for i in range(1, len(num)):
        for j in range(len(res)):
            tmp = res.pop(0)

            for k in range(len(tmp)+ 1):
                res.append(tmp[:k] + [num[i]] + tmp[k:])
    return res        

a = [1, 2, 3]
print permutations(a)


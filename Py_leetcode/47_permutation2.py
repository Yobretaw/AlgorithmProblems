import sys
import math
from collections import defaultdict

"""
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.

    For example,
    [1,1,2] have the following unique permutations:
    [1,1,2], [1,2,1], and [2,1,1].
"""
def permutations_unqiue(num):
    if not num or len(num) == 1:
        return [num] if len(num) == 1 else []

    total = len(num)
    m = defaultdict(int)
    for val in num:
        m[val] += 1

    res = []
    num = [kvp for kvp in m.iteritems()]
    permutations_unqiue_help(num, total, [], m, res)
    return res

def permutations_unqiue_help(num, total, curr, m, res):
    if len(curr) == total:
        res.append(list(curr))
        return

    for i in range(0, len(num)):
        if m[num[i][0]] > 0:
            m[num[i][0]] -= 1
            curr.append(num[i][0])
            permutations_unqiue_help(num, total, curr, m, res)
            curr.pop()
            m[num[i][0]] += 1


def permutations_unqiue_iterative(num):
    if not num or len(num) == 1:
        return [num] if num else []

    res = [[]]
    n = len(num)
    for x in num:
        new_res = []
        l = len(res[0])
        for seq in res:
            for i in range(l, -1, -1):
                if i != l and seq[i] == x:
                    break
                new_res.append(seq[:i] + [x] + seq[i:])
        res = new_res
    return res


#a = [1, 1, 2]
#a = [0, 0, 1, 1]
a = [0, 0, 1, 0, 1]
#a = [1, 2, 3, 4]
#a = [0, 0, 1, 1]
#for line in permutations_unqiue(a):
#for line in permutations_unqiue_iterative(a):
#    print line
#print permutations_unqiue(a)
#print len(permutations_unqiue(a))
#print len(permutations_unqiue_iterative(a))

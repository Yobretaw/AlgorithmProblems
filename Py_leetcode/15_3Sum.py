import sys
import math

"""
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note:
    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
    The solution set must not contain duplicate triplets.

        For example, given array S = {-1 0 1 2 -1 -4},

        A solution set is:
        (-1, 0, 1)
        (-1, -1, 2)
"""
def three_sum(a):
    n = len(a)
    a.sort()

    if n < 3:
        return []

    if n == 3:
        return [a] if sum(a) == 0 else []

    res = []
    i = 0
    while i < n - 2:
        j = i + 1
        k = n - 1

        while j < k:
            total = a[i] + a[j] + a[k]
            if total == 0:
                res.append([a[i], a[j], a[k]])
                j += 1
                k -= 1
                while j < k and a[j] == a[j - 1]: j += 1
                while j < k and a[k] == a[k + 1]: k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1

        while i < n - 1 and a[i] == a[i + 1]:
            i += 1
        i += 1

    return res


#a = [-1, 0, 1, 2, -1, -4]
#print three_sum(a)
#a = [0, 0, 0, 0]
#print three_sum(a)

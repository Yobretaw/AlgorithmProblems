import sys
import math
import imp
from collections import defaultdict

"""
    Find all possible combinations of k numbers that add up to a number n, given that only numbers
    from 1 to 9 can be used and each combination should be a unique set of numbers.

    Ensure that numbers within the set are sorted in ascending order.


    Example 1:

    Input: k = 3, n = 7

    Output:

    [[1,2,4]]

    Example 2:

    Input: k = 3, n = 9

    Output:

    [[1,2,6], [1,3,5], [2,3,4]]
"""
def combination_sum_III(k, n):
    if n > sum([i for i in range(1, 11)]):
        return []

    res = []
    sum_help(k, n, 1, [], res)
    return res


def sum_help(k, n, curr, arr, res):
    if len(arr) == k:
        if sum(arr) == n:
            res.append(list(arr))
        return

    if len(arr) > k or curr > 9:
        return


    for i in range(curr, 10):
        arr.append(i)
        sum_help(k, n, i + 1, arr, res)
        arr.pop()

#print combination_sum_III(3, 9)
#print combination_sum_III(3, 15)

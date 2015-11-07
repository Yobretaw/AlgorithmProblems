import sys
import os
import math


"""
    Write a function that takes as input a positive integer k and returns a
    list of all the strings that have k pairs of matches parens.
"""
def enumerate_balanced_parens(k):
    if k == 0:
        return ''

    res = []
    enumerate_balanced_parens_help([], 0, k, res)
    return res

def enumerate_balanced_parens_help(curr, open_count, k, res):
    n = len(curr)
    if n == 2 * k:
        res.append(''.join(curr))
        return

    closed_count = n - open_count
    if open_count < k:
        curr.append('(')
        enumerate_balanced_parens_help(curr, open_count + 1, k, res)
        curr.pop()

    if closed_count < open_count:
        curr.append(')')
        enumerate_balanced_parens_help(curr, open_count, k, res)
        curr.pop()



if __name__ == '__main__':
    for line in enumerate_balanced_parens(5):
        print line

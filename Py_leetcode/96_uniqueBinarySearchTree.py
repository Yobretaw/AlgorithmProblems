import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

    For example,
    Given n = 3, there are a total of 5 unique BST's.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
"""
def num_trees(n):
    mem = {}
    return num_trees_help(0, n, mem)

def num_trees_help(start, end, mem):
    if start >= end - 1:
        return 1

    if (start, end) in mem:
        return mem[(start, end)]
    res = 0
    for i in range(start, end):
        left_count = num_trees_help(start, i, mem)
        right_count = num_trees_help(i + 1, end, mem)
        res += left_count * right_count
    mem[(start, end)] = res
    return res

#print num_trees(19)

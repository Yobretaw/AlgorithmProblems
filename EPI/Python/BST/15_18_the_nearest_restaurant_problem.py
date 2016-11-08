import sys
import os
import imp
import math

from BST import Node, bst_print, generate_complete_bst


"""
    Write a function that takes as input a BST and a range [L, U] and returns
    a list of all keys that lie in [L, U]
"""
def range_query(root, l, u):
    if not root or l > u:
        return None

    res = []
    range_query_help(root, l, u, res)
    return res

def range_query_help(root, l, u, res):
    if not root:
        return

    if l < root.val:
        range_query_help(root.left, l, u, res)
    if l <= root.val <= u:
        res.append(root.val)
    if u > root.val:
        range_query_help(root.right, l, u, res)


if __name__ == '__main__':
    root = generate_complete_bst(15)
    bst_print(root)
    print range_query(root, 0, 15)
    print range_query(root, 5, 10)
    print range_query(root, 5, 15)


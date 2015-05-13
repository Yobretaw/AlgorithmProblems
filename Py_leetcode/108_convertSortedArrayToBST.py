import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
def array_to_bst(arr):
    if not arr:
        return None

    return array_to_bst_help(arr, 0, len(arr))


def array_to_bst_help(arr, start, end):
    if start == end:
        return None
    if start == end - 1:
        return Node(arr[start])

    mid = (start + end) / 2
    node = Node(arr[mid])
    node.left = array_to_bst_help(arr, start, mid)
    node.right = array_to_bst_help(arr, mid + 1, end)
    return node

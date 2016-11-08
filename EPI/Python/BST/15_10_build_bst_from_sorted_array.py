import sys
import os
import math
from BST import Node, bst_print


"""
    How would you build a BST of minimum possible height from a sorted array?
"""
def build_bst_from_sorted_array(arr):
    n = len(arr)
    return build_bst_from_sorted_array_help(arr, 0, n)

def build_bst_from_sorted_array_help(arr, start, end):
    if start == end:
        return None

    if start == end - 1:
        return Node(arr[start])

    mid = start + (end - start) / 2
    root = Node(arr[mid])

    root.left = build_bst_from_sorted_array_help(arr, start, mid)
    root.right = build_bst_from_sorted_array_help(arr, mid + 1, end)

    return root

if __name__ == '__main__':
    arr = [i for i in range(15)]
    bst_print(build_bst_from_sorted_array(arr))

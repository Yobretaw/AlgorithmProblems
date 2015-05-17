import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, find the maximum path sum.

    The path may start and end at any node in the tree.

    For example:
    Given the below binary tree,

           1
          / \
         2   3
    Return 6.
"""
def max_path_sum(root):
    if not root:
        return 0

    return max(max_path_sum_help(root))


def max_path_sum_help(root):
    if not root:
        return None

    left = max_path_sum_help(root.left)
    right = max_path_sum_help(root.right)

    # (canBeUsedByParent, notBeUsedByParent)
    first = root.val
    second = root.val
    if left:
        first = max(first, root.val + left[0])
        second = max(second, left[1], root.val + max(left[0], 0))
    if right:
        first = max(first, root.val + right[0])
        second = max(second, right[1], root.val + max(right[0], 0) + (left[0] if left and left[0] > 0 else 0))
    return (first, second)

root = Node(1, Node(-2), Node(3))
#root = Node(-2, Node(1))
#root = Node(-2, Node(-1))
#root = Node(2, Node(-1))
#root = Node(-2, Node(6, Node(0), Node(-6)))
print max_path_sum(root)

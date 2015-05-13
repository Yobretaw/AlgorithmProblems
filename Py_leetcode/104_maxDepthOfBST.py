import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
def max_depth(root):
    if not root:
        return 0

    return max_depth_help(root)

def max_depth_help(root):
    if not root:
        return 0

    return 1 + max(max_depth_help(root.left), max_depth_help(root.right))

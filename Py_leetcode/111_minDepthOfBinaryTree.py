import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
def min_depth(root):
    if not root:
        return 0

    if not root.left or not root.right:
        return 1 + (min_depth(root.left) if root.left else min_depth(root.right))
    else:
        return 1 + min(min_depth(root.left), min_depth(root.right))

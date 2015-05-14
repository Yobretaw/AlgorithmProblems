import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the
    depth of the two subtrees of every node never differ by more than 1.
"""
def is_balanced(root):
    if not root:
        return True

    return is_balanced_help(root)[0]

def is_balanced_help(root):
    if not root:
        return (True, 0)

    left = is_balanced_help(root.left)
    if not left[0]:
        return left
    right = is_balanced_help(root.right)
    if not right[0]:
        return right

    return (True if abs(left[1] - right[1]) < 2 else False, 1 + max(left[1], right[1]))

#root = Node(1, None, Node(2, None, Node(3)))
#print is_balanced(root)

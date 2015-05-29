import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, imagine yourself standing on the right side of it, return the values of
    the nodes you can see ordered from top to bottom.

    For example:
    Given the following binary tree,
       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
    You should return [1, 3, 4].
"""
def right_side_view(root):
    res = []
    right_side_view_help(root, 0, [0], res)
    return res

def right_side_view_help(root, curr, level, res):
    if not root:
        return

    if curr >= level[0]:
        res.append(root.val)
        level[0] += 1

    curr += 1
    right_side_view_help(root.right, curr, level, res)
    right_side_view_help(root.left, curr, level, res)


#root = Node(1, Node(2, None, Node(5)), Node(3, None, Node(4)))
#print right_side_view(root)

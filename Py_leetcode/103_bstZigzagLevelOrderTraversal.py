import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree {3,9,20,#,#,15,7},
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
"""
def zigzag_level_order_travsersal(root):
    if not root:
        return []

    q = deque()
    q.append(root)
    q.append(None)
    res = []
    curr = []
    odd_level = True
    while True:
        node = q[0]
        q.popleft()
        if not node:
            res.append(curr if odd_level else curr[::-1])
            odd_level = not odd_level
            if len(q) == 0:
                break
            else:
                q.append(None)
                curr = []
        else:
            curr.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res


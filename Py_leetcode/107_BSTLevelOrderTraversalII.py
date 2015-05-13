import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

    For example:
    Given binary tree {3,9,20,#,#,15,7},
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
"""
def level_order_traversal2(root):
    if not root:
        return []

    q = deque()
    q.append(root)
    q.append(None)
    res = []
    curr = []
    while True:
        node = q[0]
        q.popleft()
        if not node:
            res.append(curr)
            if len(q) == 0:
                break
            else:
                q.append(None)
                curr = []
        else:
            curr.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res[::-1]

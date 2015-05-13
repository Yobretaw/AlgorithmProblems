import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    For example:
    Given binary tree {3,9,20,#,#,15,7},
        3
       / \
      9  20
        /  \
       15   7
    return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]

"""
def level_order_traversal(root):
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
    return res

#root = Node(1, Node(0), Node(2))
#print level_order_traversal(root)

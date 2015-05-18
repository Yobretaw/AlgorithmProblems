import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, return the preorder traversal of its nodes' values.

    For example:
    Given binary tree {1,#,2,3},
       1
        \
         2
        /
       3
    return [1,2,3].

    Note: Recursive solution is trivial, could you do it iteratively?
"""
def preorder_traversal(root):
    if not root:
        return []

    res = []
    st = []
    push_left(st, root, res)
    while st:
        curr = st[-1]
        st.pop()
        if curr.right:
            push_left(st, curr.right, res)

    return res


def push_left(st, root, res):
    while root:
        res.append(root.val)
        st.append(root)
        root = root.left


def preorder_traversal_morris(root):
    if not root:
        return []

    res = []
    while root:
        if root.left:
            pred = root.left
            while pred.right and not pred.right is root:
                pred = pred.right
            if pred.right:
                pred.right = None
                root = root.right
            else:
                res.append(root.val)
                pred.right = root
                root = root.left
        else:
            res.append(root.val)
            root = root.right
    return res

#root = Node(1, Node(2), Node(3))
#root = Node(1)
#print preorder_traversal_morris(root)

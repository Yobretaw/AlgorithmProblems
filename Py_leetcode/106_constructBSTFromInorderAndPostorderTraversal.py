import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.
"""
def construct_bst(postorder, inorder):
    if not postorder:
        return None

    m = {}
    for i in range(0, len(inorder)):
        m[inorder[i]] = i

    return construct_bst_help(postorder, 0, len(inorder), m, [len(inorder) - 1])


def construct_bst_help(postorder, start, end, m, curr):
    if start == end:
        return None
    if start == end - 1:
        node = Node(postorder[curr[0]])
        curr[0] -= 1
        return node

    node = postorder[curr[0]]
    curr[0] -= 1

    i = m[node.val]
    node.right = construct_bst_help(postorder, i + 1, end, m, curr)
    node.left = construct_bst_help(postorder, start, i, m, curr)
    return node

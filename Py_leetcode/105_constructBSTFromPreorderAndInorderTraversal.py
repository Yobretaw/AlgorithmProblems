import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.
"""
def construct_bst(preorder, inorder):
    if not preorder:
        return None

    m = {}
    for i in range(0, len(inorder)):
        m[inorder[i]] = i
    return construct_bst_help(preorder, 0, len(preorder), m, [0])


def construct_bst_help(preorder, start, end, m, curr):
    if start == end:
        return None
    elif start == end - 1:
        node = Node(preorder[curr[0]])
        curr[0] += 1
        return node

    node = Node(preorder[curr[0]])
    curr[0] += 1
    
    i = m[node.val]
    node.left = construct_bst_help(preorder, start, i, m, curr)
    node.right = construct_bst_help(preorder, i + 1, end, m, curr)
    return node

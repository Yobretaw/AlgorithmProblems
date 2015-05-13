import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
"""
def validate_bst(root):
    if not root:
        return True

    res = [None, True]
    validate_bst_help(root, res)
    return res[1]

def validate_bst_help(root, res):
    if not root or not res[1]:
        return

    validate_bst_help(root.left, res)
    if res[0] != None and root.val <= res[0]:
        res[1] = False
    res[0] = root.val
    validate_bst_help(root.right, res)

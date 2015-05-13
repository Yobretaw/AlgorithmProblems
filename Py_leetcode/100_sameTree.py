import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given two binary trees, write a function to check if they are equal or not.

    Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
def same_tree(root1, root2):
    if not root1 or not root2:
        return root1 == None and root2 == None
    return root1.val == root2.val and same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

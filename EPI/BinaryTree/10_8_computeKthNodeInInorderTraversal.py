import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Design a function that efficiently computes the k-th node appearing in an inorde traversal.
    Assume that each node stores the number of nodes in the subtree rooted at that node.
    ============================================================================================
"""
def k_node(root, k):
    if not root or k < 1:
        return None

    left_count = root.left.count if root.left else 0
    right_count = root.right.count if root.right else 0

    if k == right_count + 1:
        return root
    elif k > right_count + 1:
        return k_node(root.right, k)
    else:
        return k_node(root.left, k - left_count - 1)


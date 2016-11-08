import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that
    each node has a parent pointer.
    ============================================================================================
"""
def compute_lca_with_parent_ptr(n1, n2):
    a = n1
    b = n2

    depth_a = 0
    depth_b = 0

    while a.parent:
        depth_a += 1
        a = a.parent

    while b.parent:
        depth_b += 1
        b = b.parent

    lower = n1 if depth_a > depth_b else n2
    higher = n1 if depth_a <= depth_b else n2

    diff = abs(depth_a - depth_b)
    while diff:
        lower = lower.parent
        diff -= 1

    while lower and not lower is higher:
        lower = lower.parent
        higher = higher.parent

    return lower

import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Consider a binary tree in which each node contains a binary digit(0 or 1). A root-to-leaf
    path can be associated with a binary number - the MSB is at the root.

    Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf
    paths.
    ============================================================================================
"""
def sum_paths(root):
    return sum_paths_help(root, root.val)


def sum_paths_help(root, curr):
    if not root:
        return 0

    if not root.left and not root.right:
        return curr

    curr <<= 1
    curr += root.val
    return sum_paths_help(root.left, curr) + sum_paths_help(root.right, curr)


#root = Node(1, Node(0, Node(0, Node(0), Node(1)), Node(1, None, Node(1, Node(0)))), Node(1, Node(0, None, Node(0, Node(1, None, Node(1)), Node(0))), Node(0, None, Node(0))))

#print sum_paths(root)
#print int('1000', 2) + int('1001', 2) + int('101110', 2) + int('110011', 2) + int('11000', 2) + int('1100', 2)

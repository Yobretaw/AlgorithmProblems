import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following is not:
        1
       / \
      2   2
       \   \
       3    3

    Note:
    Bonus points if you could solve it both recursively and iteratively.
"""
def is_symmetric(root):
    if not root:
        return True

    return is_symmetric_help(root.left, root.right)


def is_symmetric_help(left, right):
    if not left or not right:
        return left == None and right == None

    return left.val == right.val and is_symmetric_help(left.right, right.left) and is_symmetric_help(left.left, right,right)

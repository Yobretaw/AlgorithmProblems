import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Write a function which takes as input an integer and a binary tree with integer node value,
    and checks if there exists a leaf whose path sum equals the given integer.
    ============================================================================================
"""
def find_leaf(root, k):
    if not root:
        return False

    return find_leaf_help(root, 0, k)


def find_leaf_help(root, curr, k):
    if not root:
        return None

    curr += root.val

    if not root.left and not root.right:
        return root if curr == k else None

    left = find_leaf_help(root.left, curr, k)
    return left if left else find_leaf_help(root.right, curr, k)


#root = Node(314, Node(6, Node(271, Node(28), Node(0)), Node(561, None, Node(3, Node(17)))), Node(6, Node(2, None, Node(1, Node(401, None, Node(641)))), Node(271, None, Node(28))))

#print find_leaf(root, 591)

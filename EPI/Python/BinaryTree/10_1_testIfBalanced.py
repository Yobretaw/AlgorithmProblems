import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    A binary tree is said to be balanced if for each node in the tree, the difference in the
    height of its left and right subtrees is at most one.

    Write a function that takes as input the a binary tree and checks whether the tree is 
    balanced.
    ============================================================================================
"""
def is_balanced(root):
    return is_balanced_help(root)[1]

def is_balanced_help(root):
    if not root:
        return (0, True)

    if not root.left and not root.right:
        return (1, True)

    left = is_balanced_help(root.left)
    if not left[1]:
        return (-1, False)

    right = is_balanced_help(root.right)
    if not right[1]:
        return (-1, False)

    return (1 + max(left[0], right[0]), abs(left[0] - right[0]) <= 1)


root = Node(1)
print is_balanced(root)

root = Node(1, Node(2))
print is_balanced(root)

root = Node(1, Node(2), Node(3))
print is_balanced(root)

root = Node(1, Node(2, Node(4)), Node(3))
print is_balanced(root)

root = Node(1, Node(2, Node(4)), Node(3, Node(8)))
print is_balanced(root)

root = Node(1, Node(2, Node(4, Node(8))), Node(3, Node(8)))
bst_print(root)
print is_balanced(root)

root = Node(1, Node(2, Node(4, Node(8, None, Node(9)))), Node(3, Node(8)))
bst_print(root)
print is_balanced(root)

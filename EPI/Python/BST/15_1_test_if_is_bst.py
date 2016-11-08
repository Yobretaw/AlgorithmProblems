import sys
import os
import math
from BST import Node


"""
    Write a function that takes as input the root of a binary tree whose nodes
    have a key field, and returns true if and only if the tree satisfies the
    BST properties.
"""
def is_bst(root):
    return is_bst_help(root)[0]

def is_bst_help(root):
    if not root or not root.left and not root.right:
        return (True, None, None) if not root else (True, root.val, root.val)


    l, r = is_bst_help(root.left), is_bst_help(root.right)
    if not l[0] or not r[0]:
        return False, None, None
    elif l[2] and l[2] >= root.val or r[1] and r[1] <= root.val:
        return False, None, None
    else:
        return True, l[1], r[2]


def is_bst2(root):
    return is_bst_help2(root, -sys.maxint, sys.maxint)

def is_bst_help2(root, lower, upper):
    if not root:
        return True

    if not lower < root.val < upper:
        return False

    return is_bst_help2(root.left, lower, root.val) and \
            is_bst_help2(root.right, root.val, upper)


if __name__ == '__main__':
    root = Node(1, Node(0), Node(2))
    print is_bst(root)
    print is_bst2(root)

    root = Node(1, Node(2), Node(3))
    print is_bst(root)
    print is_bst2(root)

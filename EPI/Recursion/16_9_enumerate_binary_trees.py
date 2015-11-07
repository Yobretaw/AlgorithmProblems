import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    Write a function which takes as input an integer n and returns all distinct
    binary tree with n nodes.
"""
def enumerate_binary_tree(n):
    if not n:
        return None

    return enumerate_binary_tree_help(0, n)

def enumerate_binary_tree_help(start, end):
    if start >= end:
        return []

    res = []
    for i in range(start, end):
        root = Node(i)

        ltrees = enumerate_binary_tree_help(start, i)
        rtrees = enumerate_binary_tree_help(i + 1, end)

        if not ltrees and not rtrees:
            res.append(copy_bst(root))
        elif not ltrees:
            for r in rtrees:
                root.right = r
                res.append(copy_bst(root))
        elif not rtrees:
            for l in ltrees:
                root.left = l
                res.append(copy_bst(root))
        else:
            for l in ltrees:
                for r in rtrees:
                    root.left = l
                    root.righ = r
                    res.append(copy_bst(root))
    return res


def copy_bst(root):
    if not root:
        return None

    new_root = Node(root.val)
    new_root.left = copy_bst(root.left)
    new_root.right = copy_bst(root.right)

    return new_root


if __name__ == '__main__':
    for t in enumerate_binary_tree(6):
        bst_print(t)
        print '-' * 100

import sys
import os
import math
from BST import Node, bst_print


"""
    Suppose you are given the sequence in which keys are visited in an inorder
    traversal of a BST, and all keys are distinct. Can you reconstruct the BST
    from this sequence? If so, write a program to do so. Solve the same problem
    for preorder and postorder traversal sequences.

    ====

    We can reconstruct a bst from either preorder or postorder traversal but not
    inorder traversal.
"""
def reconstruct_bst_from_preorder_traversal(preorder):
    return reconstruct_bst_from_preorder_traversal_help(preorder, -sys.maxint, sys.maxint, [0])

def reconstruct_bst_from_preorder_traversal_help(preorder, lower, upper, idx):
    if idx[0] == len(preorder):
        return None

    root_val = preorder[idx[0]]
    if root_val < lower or root_val > upper:
        return None
    idx[0] += 1

    return Node(root_val,
            reconstruct_bst_from_preorder_traversal_help(preorder, lower, root_val, idx),
            reconstruct_bst_from_preorder_traversal_help(preorder, root_val, upper, idx))


def reconstruct_bst_from_postorder_traversal(postorder):
    n = len(postorder)
    return reconstruct_bst_from_postorder_traversal_help(postorder, -sys.maxint, sys.maxint, [n - 1])

def reconstruct_bst_from_postorder_traversal_help(postorder, lower, upper, idx):
    if idx[0] == -1:
        return None

    root_val = postorder[idx[0]]
    if root_val < lower or root_val > upper:
        return None

    idx[0] -= 1

    r = reconstruct_bst_from_postorder_traversal_help(postorder, root_val, upper, idx)
    l = reconstruct_bst_from_postorder_traversal_help(postorder, lower, root_val, idx)
    return Node(root_val, l, r)


if __name__ == '__main__':
    preorder = [19, 7, 3, 2, 5, 11, 17, 13, 43, 23, 37, 29, 31, 41, 47, 53]
    bst_print(reconstruct_bst_from_preorder_traversal(preorder))

    print '-' * 100

    postorder = [2, 5, 3, 13, 17, 11, 7, 31, 29, 41, 37, 23, 53, 47, 43, 19]
    bst_print(reconstruct_bst_from_postorder_traversal(postorder))

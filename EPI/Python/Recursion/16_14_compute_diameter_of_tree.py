import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print


"""
    Given a binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some
    starting node to any node in the tree along the parent-child connections.

    The path does not need to go through the root.

    For example:
    Given the below binary tree,

           1
          / \
         2   3

    Return 6.
"""
def compute_diameter(root):
    return max(compute_diameter(root))


def compute_diameter_help(root):
    if not root:
        return -sys.maxint, -sys.maxint

    if not root.left and not root.right:
        return root.val, root.val

    l0, l1 = self.compute_diameter_help(root.left)
    r0, r1 = self.compute_diameter_help(root.right)

    return max(l0, r0, max(l1, 0) + max(r1, 0) + root.val), root.val + max(0, l1, r1)


if __name__ == '__main__':
    pass

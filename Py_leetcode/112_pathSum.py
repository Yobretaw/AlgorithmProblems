import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
    up all the values along the path equals the given sum.

    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
def path_sum(root, k):
    return path_sum_help(root, k)

def path_sum_help(root, k):
    if not root:
        return False

    k -= root.val
    if not root.left and not root.right:
        return not k
    else:
        return path_sum_help(root.left, k) or path_sum_help(root.right, k)


#root = Node(1, None, Node(2))
#print path_sum(root, 1)

import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, flatten it to a linked list in-place.

    For example,
    Given

             1
            / \
           2   5
          / \   \
         3   4   6
    The flattened tree should look like:

       1
        \
         2
          \
           3
            \
             4
              \
               5
                \
                 6
"""
def flatten(root):
    if not root:
        return None

    flatten_help(root, [None])


def flatten_help(root, prev):
    if not root:
        return
    
    if prev[0]:
        prev[0].right = root

    prev[0] = root
    right = root.right
    flatten_help(root.left, prev)
    flatten_help(right, prev)
    root.left = None

#root = Node(1, Node(2, Node(3), Node(4)), Node(5, None, Node(6)))
#flatten(root)
#bst_print(root)

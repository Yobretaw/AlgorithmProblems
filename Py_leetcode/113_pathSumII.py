import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

    For example:
    Given the below binary tree and sum = 22,
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    return
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
"""
def path_sum2(root, k):
    if not root:
        return []

    res = []
    path_sum2_help(root, k, [], res)
    return res


def path_sum2_help(root, k, curr, res):
    if not root:
        return

    k -= root.val
    if not root.left and not root.right:
        if not k:
            res.append(list(curr + [root.val]))
    else:
        curr.append(root.val)
        path_sum2_help(root.left, k, curr, res)
        path_sum2_help(root.right, k, curr, res)
        curr.pop()


#root = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, Node(5), Node(1))))
#for line in path_sum2(root, 22):
#    print line

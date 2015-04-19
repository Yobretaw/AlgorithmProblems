import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Define a node in a binary tree to be k-balanced if the difference in the number of nodes
    in its left and right substree in no more than k.

    Design an algorithm that takes as input a binary tree and positive integer k, and returns
    a node in the binary tree such that the node is not k-balanced but al of its descendants
    are k-balanced. If no such node exists, return None.
    ============================================================================================
"""
def find_k_balanced_node(root, k):
    return find_k_balanced_node_help(root, k)[1]

def find_k_balanced_node_help(root, k):
    if not root:
        return (0, None)

    if not root.left and not root.right:
        return (1, None)

    left = find_k_balanced_node_help(root.left, k)
    if left[1] != None:
        return left

    right = find_k_balanced_node_help(root.right, k)
    if right[1] != None:
        return right

    diff = abs(left[0] - right[0])
    if diff <= k:
        return (1 + max(left[0], right[0]), None)
    else:
        return (-1, root)

#root = Node(314, Node(6, Node(271, Node(28), Node(0)), Node(561, None, Node(3, Node(17)))), Node(6, Node(2, None, Node(1, Node(401, None, Node(641)))), Node(271, None, Node(28))))

#bst_print(root)
#print find_k_balanced_node(root, 2)

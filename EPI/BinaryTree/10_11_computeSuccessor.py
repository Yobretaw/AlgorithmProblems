import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    Design an algorithm that computes the successor of a node in a binary tree. Assume
    that each node stores its parent.
"""
def compute_successor(root, target):
    if not root or not target:
        return None

    if target.right:
        res = target.right
        while res.left:
            res = res.left
        return res
    else:
        return compute_successor_help(root, target)

def compute_successor_help(root, target):
    if not root:
        return None

    if root.left is target:
        return root

    if root.left:
        pred = root.left
        while pred.right:
            pred = pred.right
        if pred is target:
            return root

    left = compute_successor_help(root.left, target)
    return left if left else compute_successor_help(root.right, target)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n6
n4.right = n5

bst_print(n1)
print compute_successor(n1, n1)
print compute_successor(n1, n2)
print compute_successor(n1, n3)
print compute_successor(n1, n4)
print compute_successor(n1, n5)
print compute_successor(n1, n6)

import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    The exterior of a binary tree is the following sequence of nodes: the nodes from the root to the
    left most leaf, followed by the leaves in left-to-right order, followed by the nodes from the
    rightmost leaf to the root.

    Write a function that computes the exterior of a binary tree.
"""
def compute_exterior(root):
    if not root:
        return []

    seq = []
    flag = [0]
    compute_exterior_help(root, seq, flag)

    right = []
    while root:
        right.append(root.val)
        root = root.right
    right[:] = right[::-1]

    return seq + right

def compute_exterior_help(root, seq, flag):
    if not root:
        return

    if flag[0] == 0 and root != None:
        seq.append(root.val)
        if not root.left:
            flag[0] += 1
    elif flag[0] == 1 and root.left == None and root.right == None:
        seq.append(root.val)

    compute_exterior_help(root.left, seq, flag)
    compute_exterior_help(root.right, seq, flag)


#root = Node(1, Node(0, Node(-1), Node(-2)), Node(2, Node(1.5), Node(2.5)))
#print compute_exterior(root)

import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    Many different binary trees have the same preorder traversal sequence.
    
    In this problem, the preorder traversal computation is modified to mark where a left or right child is empty.

    Design an algorithm for reconstructing a binary tree from a preorder traversal visit sequence that uses None
    to mark empty children.
"""
def reconstruct(seq):
    n = len(seq)
    if n < 2:
        return None if n == 0 else Node(seq[0])

    return reconstruct_help(seq, [0])

def reconstruct_help(seq, idx):
    n = len(seq)
    if seq[idx[0]] == None:
        idx[0] += 1
        return None

    root = Node(seq[idx[0]])
    idx[0] += 1
    root.left = reconstruct_help(seq, idx)
    root.right = reconstruct_help(seq, idx)
    return root

seq = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]
root = reconstruct(seq)
bst_print(root)

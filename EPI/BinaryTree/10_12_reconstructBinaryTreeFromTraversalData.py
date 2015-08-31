import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    Given an inorder traversal sequence and one of any other traversal sequence of a binary
    tree, there exists a unique binary tree that yields those orders, assuming each node
    holds a distinct key.

    Given an inorder traversal sequence and a preorder traversal sequence of a binary tree,
    write a function to reconstruct the tree. Assuming each node has a unique key.
"""
def reconstruct(inorder, preorder):
    n = len(preorder)

    if n == 0:
        return None

    if n == 1:
        return Node(preorder[0])

    root = Node(preorder[0])
    root_idx = inorder.index(root.val)
    root.left = reconstruct(inorder[:root_idx], preorder[1:1+root_idx])
    root.right = reconstruct(inorder[root_idx + 1:], preorder[1+root_idx:])
    return root

"""
    Optimized solution that takes O(n) time
"""
def reconstruct2(inorder, preorder):
    m = {}
    for i in range(0, len(inorder)):
        m[inorder[i]] = i

    curr = [0]
    return reconstruct2_help(preorder, m, 0, len(preorder) - 1, curr)

def reconstruct2_help(preorder, m, start, end, curr):
    if start > end:
        return None

    root = Node(preorder[curr[0]])
    curr[0] += 1
    root_idx = m[root.val]
    root.left = reconstruct2_help(preorder, m, start, root_idx - 1, curr)
    root.right = reconstruct2_help(preorder, m, root_idx + 1, end, curr)
    return root


#inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
#preorder = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
#bst_print(reconstruct(inorder, preorder))
#print '-' * 100
#bst_print(reconstruct2(inorder, preorder))

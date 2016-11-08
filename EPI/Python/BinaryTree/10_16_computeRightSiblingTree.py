import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    For this problem, assume that a binary tree node has a 'next' field that holds a binary
    tree node(this field is distinct from the left and right children). This field will be
    used to compute a map from ndoes to their right sibilngs. The input is assumed to be a
    perfect binary tree.

    Write a function that takes a perfect binary tree, and sets each node's 'next' field to
    the node on its right, if one exists.
"""
def compute_right_sibling_tree(root):
    if not root:
        return

    if not root.left:
        return

    next_root = root.left
    prev = root.left
    curr = root.right

    while True:
        prev.next = curr
        prev = curr

        root = root.next
        if not root:
            break

        prev.next = root.left
        prev = root.left
        curr = root.right

    root = next_root
    compute_right_sibling_tree(root)


#root = Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6)))
#bst_print(root)
#compute_right_sibling_tree(root)
#while root:
#    next_root = root.left
#    while root:
#        print root
#        root = root.next
#    root = next_root

import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Write a function that checks whether a binary tree is symmetric.
    ============================================================================================
"""
def is_symmetric(root):
    if not root:
        return True

    return is_symmetric_help(root.left, root.right)

def is_symmetric_help(left, right):
    if not left and not right:
        return True

    if left == None or right == None:
        return False

    if left.val != right.val:
        return False

    return is_symmetric_help(left.left, right.right) and is_symmetric_help(left.right, right.left)


#root = Node(1, Node(2, None, Node(3, None, Node(4))), Node(2, Node(3, Node(4))))
#bst_print(root)
#print is_symmetric(root)

#root = Node(1, Node(2, None, Node(3, Node(-1), Node(4))), Node(2, Node(3, Node(4))))
#bst_print(root)
#print is_symmetric(root)

#root = Node(1, Node(2, None, Node(3, Node(4))), Node(2, Node(3, Node(4, Node(1)))))
#bst_print(root)
#print is_symmetric(root)

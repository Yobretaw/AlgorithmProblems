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
def compute_successor(node):
    if node.right:
        res = node.right
        while res.left:
            res = res.left
        return res
    else:
        if not node.parent:
            return None
        else:
            parent = node.parent
            if parent.left is node:
                return parent
            else:
                while parent and parent.right is node:
                    parent, node = parent.parent, node.parent
                return parent


root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

root.left = n2
root.right = n3

n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

n2.parent = root
n3.parent = root
n4.parent = n2
n5.parent = n2
n6.parent = n3
n7.parent = n3

bst_print(root)
print compute_successor(root)
print compute_successor(n2)
print compute_successor(n3)
print compute_successor(n4)
print compute_successor(n5)
print compute_successor(n6)
print compute_successor(n7)

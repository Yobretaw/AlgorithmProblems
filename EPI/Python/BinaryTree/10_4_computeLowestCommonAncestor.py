import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ===========================================================================
    Design an algorithm for computing the Lowest Common Ancestor(LCA) of two
    nodes in a binary tree in which nodes do not have a parent field.
    ===========================================================================
"""
def find_lca(root, n1, n2):
    if not root:
        return None

    if root is n1 or root is n2:
        return root

    l = find_lca(root.left, n1, n2)
    r = find_lca(root.right, n1, n2)

    if l and r:
        return root

    return l if l else r


#n1 = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)

#n1.left = n2
#n1.right = n3
#n2.left = n4
#n2.right = n6
#n4.right = n5

#print find_lca(n1, n5, n6)

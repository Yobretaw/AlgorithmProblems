import os
import math
import sys
from collections import defaultdict, Counter

Node = imp.load_source('Node', '../BST/BST.py').Node

"""
    Design an algorithm for computing the LCA of two nodes in a binary tree.
    The algorithm's time complexity should depend only on distance from the
    nodes to the LCA.

    Assume each node in the tree has a parent pointer.
"""
def find_lca(root, node_a, node_b):
    if not root:
        return None

    if not node_a or not node_b:
        return node_a if not node_b else node_b

    d = {}
    while node_a or node_b:
        if node_a == node_b:
            return node_a
        elif node_a in d or node_b in d:
            return node_a if node_a in d else node_b

        d[node_a] = 1
        d[node_b] = 1

        if node_a:
            node_a = node_a.parent
        if node_b:
            node_b = node_b.parent

    return root



#class LCA_Finder:
#    def __init__(self, tree):
#        if tree:
#            self.comsuming_tree(tree)

#    def comsuming_tree(self, root):
#        self.d = {}
#        self.comsuming_tree_help(root, 0)

#    def comsuming_tree_help(self, root, depth):
#        if not root:
#            return

#        self.d[root] = depth
#        comsuming_tree_help(root.left, depth + 1)
#        comsuming_tree_help(root.right, depth + 1)

#    def find_lca(self, node_a, node_b):
#        depth_a = self.d[node_a]
#        depth_b = self.d[node_b]
        
#        lower_node = node_a if depth_a > depth_b else node_b
#        upper_node = node_a if depth_a <= depth_b else node_b
#        for i in range(abs(depth_b - depth_a)):
#            lower_node = lower_node.parent

#        while lower_node != upper_node:
#            lower_node, upper_node = lower_node.parent, upper_node.parent

#        return lower_node

import sys
import heapq
import imp
from collections import defaultdict, deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print
generate_complete_bst = imp.load_source('Node', '../EPI/BST/BST.py').generate_complete_bst

"""
    Given a complete binary tree, count the number of nodes.

    Definition of a complete binary tree from Wikipedia:

    In a complete binary tree every level, except possibly the last, is
    completely filled, and all nodes in the last level are as far left as
    possible. It can have between 1 and 2^h nodes inclusive at the last level h.
"""
def count_complete_tree_nodes(root):
    h = compute_depth(root)
    nodes = 0
    while root:
        if compute_depth(root.right) == h - 1:
            nodes += 2 ** h
            root = root.right
        else:
            nodes += 2 ** (h - 1)
            root = root.left
        h -= 1
    return nodes

def compute_depth(root):
    count = 0
    while root:
        root = root.left
        count += 1

    return count - 1

if __name__ == '__main__':
    for i in range(1, 500):
        if not count_complete_tree_nodes(generate_complete_bst(i)) == i:
            print i

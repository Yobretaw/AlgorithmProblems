import sys
import os
import math

from BST import Node, bst_print, generate_complete_bst, find_node


"""
    Define a binary tree with integer-labeled nodes to be an almost BST if it
    does not satisfy the BST property, but there exists a pair of nodes such
    that swapping the keys at the nodes makes resulting binary tree a BST.

    Design an algorithm that takes as input a binary tree with integer-labeled
    nodes, and determine if it is an almost BST. If it is an almost BST, recon-
    strucdt the original BST.
"""
def test_and_reconstruct_almost_bst(root):
    prev = [None]
    swap_nodes = []
    test_and_reconstruct_almost_bst_help(root, prev, swap_nodes)

    if len(swap_nodes) != 2:
        return False

    a, b = swap_nodes[0], swap_nodes[1]
    a.val, b.val = b.val, a.val
    return True

def test_and_reconstruct_almost_bst_help(root, prev, swap_nodes):
    if not root:
        return

    test_and_reconstruct_almost_bst_help(root.left, prev, swap_nodes)
    if prev[0]:
        if root.val < prev[0].val:
            if not swap_nodes:
                swap_nodes.append(prev[0])
            else:
                swap_nodes.append(root)
    prev[0] = root
    test_and_reconstruct_almost_bst_help(root.right, prev, swap_nodes)


if __name__ == '__main__':
    root = Node(17,
            Node(41,
                None,
                Node(8,
                    Node(6),
                    None)),
            Node(23,
                Node(21),
                Node(5,
                    Node(30),
                    None)))
    bst_print(root)
    print test_and_reconstruct_almost_bst(root)
    bst_print(root)

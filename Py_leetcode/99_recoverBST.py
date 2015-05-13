import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Two elements of a binary search tree (BST) are swapped by mistake.

    Recover the tree without changing its structure.

    Note:
    A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
def recover_bst(root):
    if not root:
        return

    nodes = [None, None, None]    # [preNode, changeNode, secondChangeNode]
    recover_bst_help(root, nodes)
    nodes[1].val, nodes[2].val = nodes[2].val, nodes[1].val


def recover_bst_help(root, nodes):
    if not root:
        return

    recover_bst_help(root.left, nodes)
    if not nodes[0] or root.val > nodes[0].val:
        nodes[0] = root
        recover_bst_help(root.right, nodes)
    else:
        if nodes[1]:
            nodes[2] = root
        else:
            nodes[1], nodes[2], nodes[0] = nodes[0], root, root
            recover_bst_help(root.right, nodes)

#root = Node(0, Node(1))
#root = Node(5, Node(3, Node(1), Node(6)), Node(7, Node(4), Node(8)))
#root = Node(1, Node(2), Node(3))
#root = Node(1, None, Node(2, Node(3)))
#bst_print(root)
#print '-' * 100
#recover_bst(root)
#bst_print(root)

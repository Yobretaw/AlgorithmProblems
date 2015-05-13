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

    data = [None, None, False]
    recover_bst_help(root, data)
    print data
    if not data[2] and data[1]:
        data[0].val, data[1].val = data[1].val, data[0].val


def recover_bst_help(root, data):
    if not root:
        return

    recover_bst_help(root.left, data)
    if not data[0]:
        data[0] = root
        recover_bst_help(root.right, data)
    elif root.val < data[0].val:
        if not data[1]:
            data[1] = data[0]
            data[0] = root
            recover_bst_help(root.right, data)
        else:
            data[1].val, root.val = root.val, data[1].val
            data[2] = True
    else:
        data[0] = root
        recover_bst_help(root.right, data)

root = Node(0, Node(1))
root = Node(5, Node(3, Node(1), Node(6)), Node(7, Node(4), Node(8)))
root = Node(1, Node(2), Node(3))
root = Node(1, None, Node(2, Node(3)))
bst_print(root)
print '-' * 100
recover_bst(root)
bst_print(root)

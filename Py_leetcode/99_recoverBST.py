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

    data = {}
    recover_bst_help(root, data)


def recover_bst_help(root, data):
    if not root:
        return

    recover_bst_help(root.left, data)
    if not 'preNode' in data:
        data['preNod'] = root
    elif not 'changeNode' in data and root.val < data['prevNode'].val:
        data['changeNode'] = data['prevNode']
    elif 'changeNode' in data and root.val < data['prevNode'].val:
        root.val, data['changeNode'].val = data['changeNode'].val, root.val
    else:
        data['prevNode'] = root
        recover_bst_help(root.right, data)


root = Node(0)
root.left = Node(1)
bst_print(root)
recover_bst(root)
bst_print(root)

import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Follow up for problem "Populating Next Right Pointers in Each Node".

    What if the given tree could be any binary tree? Would your previous solution still work?

    Note:

    You may only use constant extra space.
    For example,
    Given the following binary tree,
             1
           /  \
          2    3
         / \    \
        4   5    7
    After calling your function, the tree should look like:
             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \    \
        4-> 5 -> 7 -> NULL
"""
def connect2(root):
    while root:
        while root and not root.left and not root.right:
            root = root.next
        if not root:
            break
        next_head = root.left if root.left else root.right
        prev = next_head
        curr = None
        while True:
            while root and (not root.left or root.left is prev) and (not root.right or root.right is prev):
                root = root.next
            if not root:
                break
            curr = root.left if root.left and root.left != prev else root.right
            if root.right is curr:
                root = root.next
            prev.next = curr
            prev = curr
            curr = curr.next
        root = next_head

root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
connect2(root)
bst_print(root)

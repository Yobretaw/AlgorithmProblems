import sys
import os
import math
import imp

from stack import Stack
Node = imp.load_source('Node', '../BST/BST.py').Node

"""
    ============================================================================================
    Given a BST node, print all keys at that node and its descendants. The nodes should be
    printed in sorted order, and you cannot use recurrsion.
    ============================================================================================
"""
def print_keys(root):
    if not root:
        return

    s = Stack()
    push_all_left_nodes(s, root)
    while not s.empty():
        curr = s.top()
        s.pop()

        print curr.val
        push_all_left_nodes(s, curr.right)


def push_all_left_nodes(s, root):
    while root:
        # if print in descending order, add 'print root.val' here
        s.push(root)
        root = root.left

#root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
#print_keys(root)

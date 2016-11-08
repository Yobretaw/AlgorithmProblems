import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    This problem is concerned with the design of an API for setting the state of
    nodes in a binary tree to lock or unlock. A node's state cannot be set to
    lock if any of its descendants or ancestors are in lock.

    Changing a node's state to lock does not change the state of any other nodes.
    For example, all leaves may simultaneously be in state lock.

    Write the following methods for a binary tree node class:
        1. A function to test if the node is locked.
        2. A function to lock the node. If the node cannot be locked, return
        false. Otherwise lock it and return true.
        3. A function to unlock the node.

    Assume each node has a parent field.
"""
def is_locked(node):
    return node.locked

def lock_node(node):
    if not node:
        return False

    p = node.parent
    while p:
        if p.locked:
            return False
        p = p.parent
    node.locked = True
    return True

def unlock_node(node):
    node.locked = False

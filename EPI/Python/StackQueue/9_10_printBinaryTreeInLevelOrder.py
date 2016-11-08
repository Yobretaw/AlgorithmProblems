import sys
import os
import math
import imp

from stack import Stack, Queue
Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    ============================================================================================
    Design an algorithm that prints a binary tree in level order.
    ============================================================================================
"""
def level_order_print(root):
    q = Queue()
    q.enqueue(root)
    q.enqueue(None)

    s = ""
    while not q.empty():
        curr = q.dequeue()
        if not curr:
            if q.empty():
                if len(s) > 0:
                    print s.strip()
                    return
            else:
                q.enqueue(None)
                print s.strip()
                s = ""
        elif curr:
            s += str(curr.val) + " "
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)


root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
level_order_print(root)

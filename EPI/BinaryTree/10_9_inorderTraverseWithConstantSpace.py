import sys
import math
import imp
from collections import defaultdict

Node = imp.load_source('Node', '../BST/BST.py').Node
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print
"""
    Write a nonrecursive program for performing an inorder traversal on a binary
    tree. Assume nodes have parent fields.
"""
def inorder_traverse_with_parent(root):
    if not root:
        return

    curr = root
    prev = None
    while curr:
        next_node = None
        if prev == curr.parent:
            next_node = curr.left
        elif prev == curr.left:
            print curr.val
            next_node = curr.right
        else:
            next_node = curr.parent

        # leaf node
        if not next_node and prev is curr.parent:
            print curr.val
            next_node = curr.parent

        prev = curr
        curr = next_node

root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)


root.left = n2
root.right = n3

n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

n2.parent = root
n3.parent = root
n4.parent = n2
n5.parent = n2
n6.parent = n3
n7.parent = n3

bst_print(root)
inorder_traverse_with_parent(root)

"""
    Variant 10.9.1: How would you perform inorder, preorder and postorder traversals iteratively using O(1)
    space addition space? Your algorithm cannot modify the tree. Nodes have an explict parent field.
"""
def inorder_traverse(root):
    if not root:
        return

    curr = root
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            if pred.right:
                pred.right = None
                print curr.val
                curr = curr.right
            else:
                pred.right = curr
                curr = curr.left
        else:
            print curr.val
            curr = curr.right

#bst_print(root)
#inorder_traverse(root)

def preorder_traverse(root):
    if not root:
        return

    curr = root
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            if pred.right:
                pred.right = None
                curr = curr.right
            else:
                print curr.val
                pred.right = curr
                curr = curr.left
        else:
            print curr.val
            curr = curr.right

#bst_print(root)
#preorder_traverse(root)

def postorder_traverse(root):
    if not root:
        return

    dummy = Node('*')
    dummy.left = root
    curr = dummy
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right and not pred.right is curr:
                pred = pred.right
            if not pred.right:
                pred.right = curr
                curr = curr.left
            else:
                visit_reverse(curr.left, pred)
                pred.right = None
                curr = curr.right
        else:
            curr = curr.right


def visit_reverse(from_node, to_node):
    curr = to_node
    reverse_path(from_node, to_node)
    while True:
        print curr.val
        if curr == from_node:
            break
        curr = curr.right
    reverse_path(to_node, from_node)


def reverse_path(from_node, to_node):
    x = from_node
    y = from_node.right

    while not x is to_node:
        z = y.right
        y.right = x
        x = y
        y = z

#bst_print(root)
#postorder_traverse(root)

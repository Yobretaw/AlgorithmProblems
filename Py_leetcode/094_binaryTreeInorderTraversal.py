import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
Stack = imp.load_source('Node', '../EPI/StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, return the inorder traversal of its nodes' values.

    For example:
    Given binary tree {1,#,2,3},
       1
        \
         2
        /
       3
    return [1,3,2].

    Note: Recursive solution is trivial, could you do it iteratively?
"""
def inorder_traverse(root):
    if not root:
        return []

    return inorder_traverse(root.left) + [root.val] + inorder_traverse(root.right)


def inorder_traverse_iterative(root):
    if not root:
        return

    st = []
    res = []
    curr = root
    while True:
        if curr:
            push_left(st, curr)

        curr = st[-1]
        st.pop()
        res.append(curr.val)
        curr = curr.right

        if not st and not curr:
            break
    return res

def push_left(st, root):
    while root:
        st.append(root)
        root = root.left


#n1 = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)

#n1.left = n2
#n1.right = n3
#n2.left = n4
#n2.right = n6
#n4.right = n5

#bst_print(n1)
#print inorder_traverse(n1)
#inorder_traverse_iterative(n1)

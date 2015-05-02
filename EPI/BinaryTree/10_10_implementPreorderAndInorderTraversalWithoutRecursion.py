import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    Write a function which takes as input a binary tree and performs a preorder traversal of the tree.
    Do not use recursion. Nodes do not contain parent references. Do the same for a postorder traversal.
"""
def preorder_traverse(root):
    if not root:
        return

    st = Stack()
    push_left(root, st)
    while not st.empty():
        curr = st.top()
        st.pop()
        print curr.val
        if curr.right:
            push_left(curr.right, st)

        

def push_left(root, st):
    while root:
        st.push(root)
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
#preorder_traverse(n1)

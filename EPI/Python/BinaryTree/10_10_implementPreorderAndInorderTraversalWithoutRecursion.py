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
def inorder_traverse(root):
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


def preorder_traverse(root):
    if not root:
        return

    st = Stack()
    push_left_preorder(root, st)
    while not st.empty():
        curr = st.top()
        st.pop()
        if curr.right:
            push_left_preorder(curr.right, st)


def push_left_preorder(root, st):
    while root:
        print root.val
        st.push(root)
        root = root.left


def postorder_traverse_two_stacks(root):
    """
        Idea:

        1. Push root to the first stack
        2. Loop while first stack is not empty
            2.1 Pop a node from first stack and push it to the second stack
            2.2 Push left and right children of the poped ndoe to first stack
        3. Print contents of second stack
    """
    if not root:
        return

    st1 = Stack()
    st2 = Stack()
    
    st1.push(root)
    while not st1.empty():
        curr = st1.top()
        st1.pop()
        st2.push(curr)
        if curr.left:
            st1.push(curr.left)
        if curr.right:
            st1.push(curr.right)

    while not st2.empty():
        print st2.top()
        st2.pop()

def postorder_traverse_one_stacks(root):
    """
        Idea:

        1. Create an empty stack
        2. Do following while root is not None:
            2.1 Push root's right child and then root to the stack
            2.2 Set root as root's left child
        3. Pop an item from stack and set it as root.
            a) If the poped item has a right child and the rightchild
               is at top of stack, then remove the right child from stack,
               push the root back and set root as root's right child.
            b) Else print root's data and set root as None
        4. Repeat step 2 and 3 while stack is not empty
    """
    if not root:
        return

    st = Stack()
    while True:
        while root:
            if root.right:
                st.push(root.right)
            st.push(root)
            root = root.left
        root = st.top()
        st.pop()
        if not st.empty() and root.right is st.top():
            right_child = st.top()
            st.pop()
            st.push(root)
            root = right_child
        else:
            print root.val
            root = None
        if st.empty():
            break


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
#inorder_traverse(n1)
#print '-' * 100
#preorder_traverse(n1)
#print '-' * 100
##postorder_traverse_two_stacks(n1)
##postorder_traverse_one_stacks(n1)


"""
    Variant 10.10.2: Implemenet the three traversals of a binary tree without recursion and
    O(1) space. assuming each node has a reference to its parent.
"""
def inorder_traverse_with_parent(root):
    if not root:
        return

    prev = None
    curr = root
    while curr:
        tmp = curr
        if prev is curr.parent:
            if curr.left:
                curr = curr.left
            else:
                print curr.val
                curr = curr.right if curr.right else curr.parent
        elif prev is curr.left:
            print curr.val
            curr = curr.right if curr.right else curr.parent
        else:
            curr = curr.parent
        prev = tmp
                

def preorder_traverse_with_parent(root):
    if not root:
        return

    prev = None
    curr = root
    while curr:
        tmp = curr
        if prev is curr.parent:
            print curr.val
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right if curr.right else curr.parent
        elif prev is curr.left:
            curr = curr.right if curr.right else curr.parent
        else:
            curr = curr.parent
        prev = tmp


def postorder_traverse_with_parent(root):
    if not root:
        return

    prev = None
    curr = root
    while curr:
        tmp = curr
        if prev is curr.parent:
            if not curr.left and not curr.right:
                print curr.val
                curr = curr.parent
            else:
                curr = curr = curr.left if curr.left else curr.right
        elif prev is curr.left:
            if curr.right:
                curr = curr.right
            else:
                print curr.val
                curr = curr.parent
        else:
            print curr.val
            curr = curr.parent
        prev = tmp


#root = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)
#n7 = Node(7)

#root.left = n2
#root.right = n3

#n2.left = n4
##n2.right = n5
#n3.left = n6
#n3.right = n7

#n2.parent = root
#n3.parent = root
#n4.parent = n2
#n5.parent = n2
#n6.parent = n3
#n7.parent = n3

#bst_print(root)
#inorder_traverse_with_parent(root)
#print '-' * 100
#preorder_traverse_with_parent(root)
#print '-' * 100
#postorder_traverse_with_parent(root)

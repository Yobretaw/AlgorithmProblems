import sys
import math
import imp
from collections import defaultdict

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree, return the postorder traversal of its nodes' values.

    For example:
    Given binary tree {1,#,2,3},
       1
        \
         2
        /
       3
    return [3,2,1].

    Note: Recursive solution is trivial, could you do it iteratively?
"""
def postorder_traverse_one_stack(root):
    if not root:
        return []

    res = []
    st1 = [root]
    while st1:
        curr = st1[-1]
        st1.pop()
        res.append(curr.val)
        if curr.left: st1.append(curr.left)
        if curr.right: st1.append(curr.right)

    return res[::-1]


def postorder_traverse_one_stack2(root):
    if not root:
        return []

    res = []
    st = []
    curr = root
    while True:
        while curr:
            if curr.right:
                st.append(curr.right)
            st.append(curr)
            curr = curr.left

        curr = st[-1]
        st.pop()

        if st and curr.right is st[-1]:
            right_child = st[-1]
            st.pop()
            st.append(curr)
            curr = right_child
        else:
            res.append(curr.val)
            curr = None

        if not st:
            break
    return res

def postorder_traverse_morris(root):
    if not root:
        return []

    res = []
    curr = Node('*')
    curr.left = root
    while curr:
        if curr.left:
            pred = curr.left
            while pred.right and not pred.right is curr:
                pred = pred.right
            if pred.right:
                read_path(curr.left, pred, res)
                pred.right = None
                curr = curr.right
            else:
                pred.right = curr
                curr = curr.left
        else:
            curr = curr.right
    return res

def read_path(from_node, to_node, res):
    i = len(res)
    while not from_node is to_node.right:
        res.append(from_node.val)
        from_node = from_node.right
    res[i:] = res[i:][::-1]


root = Node(1, Node(2), Node(3))
#print postorder_traverse_one_stack(root)
print postorder_traverse_morris(root)

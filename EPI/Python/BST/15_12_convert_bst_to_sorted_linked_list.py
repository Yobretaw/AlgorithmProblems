import sys
import os
import math
import imp

from BST import Node, bst_print, generate_complete_bst

"""
    Design an algorithm that takes as input a BST B and returns a sorted doubly
    linked list on the same elements. Your algorithm should not allocate any
    new nodes. The original BST does not have to be preserved; use its nodes as
    the nodes of the resulting list(i.e., use 'left' and 'right' as 'prev' and
    'next' respectively).
"""
def convert_bst_to_doubly_linked_list(root):
    if not root:
        return None

    prev = [None]
    head = [None]
    convert_bst_to_doubly_linked_list_help(root, prev, head)
    return head[0]


def convert_bst_to_doubly_linked_list_help(curr, prev, head):
    if not curr:
        return None

    convert_bst_to_doubly_linked_list_help(curr.left, prev, head)

    if head[0] is None:
        head[0] = prev[0] = curr
    else:
        prev[0].right = curr
        curr.left = prev[0]

    next_node = curr.right
    curr.right = head[0]
    prev[0] = prev[0].right
    convert_bst_to_doubly_linked_list_help(next_node, prev, head)


if __name__ == '__main__':
    root = generate_complete_bst(15)
    bst_print(root)
    l = convert_bst_to_doubly_linked_list(root)
    head = l
    while l.right != head:
        print l
        l = l.right
    print l

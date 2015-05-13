import sys
import os
import math
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

ListNode = imp.load_source('ListNode', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('ListNode', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
def linkedlist_to_bst(head):
    if not head:
        return None

    l = 0
    copy = head
    while copy:
        copy = copy.next 
        l += 1
    return linkedlist_to_bst(0, l, [head])

def linkedlist_to_bst_help(start, end, curr):
    if start == end:
        return None
    if start == end - 1:
        node = Node(curr[0].val)
        curr[0] = curr[0].next
        return node

    mid = (start + end) / 2
    left = linkedlist_to_bst_help(start, mid, curr)
    node = Node(curr[0].val)
    curr[0] = curr[0].next
    right = linkedlist_to_bst_help(mid + 1, end, curr)
    node.left = left
    node.right = right
    return node

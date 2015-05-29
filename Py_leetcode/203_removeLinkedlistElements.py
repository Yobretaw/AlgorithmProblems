import sys
import os
import re
import imp
from collections import deque

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Remove all elements from a linked list of integers that have value val.

    Example
    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5
"""
def remove_elements(head, val):
    if not head:
        return None

    dummy = Node('*')
    dummy.next = head

    prev = dummy
    curr = prev.next

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummy.next


#l = Node(1, Node(1))
#print l
#print remove_elements(l, 1)

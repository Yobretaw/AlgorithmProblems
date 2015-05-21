import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    For example,
    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.
"""
def remove_dup(head):
    if not head or not head.next:
        return head

    curr = head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head


#l = Node(1, Node(2))
#l = Node(1, Node(1, Node(2, Node(2, Node(3)))))
#print remove_dup(l)

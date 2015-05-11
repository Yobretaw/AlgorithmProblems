import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a linked list and a value x, partition it such that all nodes less than x come
    before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

    For example,
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.
"""
def partition_list(head, x):
    if not head or not head.next:
        return head

    new_head = None
    dummy = Node('*')
    dummy.next = head

    prev, curr = dummy, dummy.next
    large_head, prev_large = None, None
    while curr:
        if curr.val < x:
            if not new_head:
                new_head = curr
            else:
                prev.next = curr
            prev = curr
        else:
            if not large_head:
                large_head = curr
            else:
                prev_large.next = curr
            prev_large = curr
        curr = curr.next

    if prev_large and prev_large.next and prev_large.next.val < x:
        prev_large.next = None

    prev.next = large_head
    return new_head if new_head else large_head

#l = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
#l = Node(1, Node(1))
#print partition_list(l, 0)

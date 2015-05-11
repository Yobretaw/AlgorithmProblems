import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

    For example,
    Given 1->2->3->3->4->4->5, return 1->2->5.
    Given 1->1->1->2->3, return 2->3.
"""
def remove_dup2(head):
    if not head or not head.next:
        return head

    dummy = Node('*')
    dummy.next = head

    prev = dummy
    curr = prev.next
    while curr:
        val = curr.val
        if curr.next and curr.next.val == val:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next
    return dummy.next


#l = Node(1, Node(2))
#l = Node(1, Node(1, Node(2, Node(2, Node(3)))))
#print remove_dup2(l)

import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln,
    reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

    You must do this in-place without altering the nodes' values.

    For example,
    Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
# @param {ListNode} head
# @return {void} Do not return anything, modify head in-place instead.
def reorder_list(head):
    if not head or not head.next:
        return

    premid = None
    mid = end = head
    while end and end.next:
        premid = mid if not premid else premid.next
        mid, end = mid.next, end.next.next
    if end:
        premid, mid = premid.next, mid.next

    # reverse second half of the list
    premid.next = None
    prev = None
    curr = mid
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    new_head = prev

    curr = head
    while curr and new_head:
        tmp = curr.next
        tmp2 = new_head.next
        curr.next = new_head
        new_head.next = tmp
        curr = tmp
        new_head = tmp2

#l = ll_generate_ascending_list(3, 1)
##print l
#reorder_list(l)
#print l


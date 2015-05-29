import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Reverse a singly linked list.

    click to show more hints.

    Hint:
    A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
def reverse_list(head):
    if not head or not head.next:
        return head

    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev

def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    tail = head.next
    head.next = None
    rest = reverse_list_recursive(tail)
    tail.next = head

    return rest


#l = ll_generate_ascending_list(10, 1)
#print reverse_list_recursive(l)

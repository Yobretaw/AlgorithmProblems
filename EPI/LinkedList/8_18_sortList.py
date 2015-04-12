import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function that takes as input a singly linked list whose nodes hold integer keys and
    sorts the list.
    ============================================================================================
"""
def sort_list(l):
    if not l or not l.next:
        return l

    slow = Node('*', l)
    fast = l
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    rest = slow.next
    slow.next = None

    l = sort_list(l)
    rest = sort_list(rest)

    # merge two sorted list
    dummy = Node('*')
    curr = dummy
    while l and rest:
        if l.val < rest.val:
            curr.next = l
            l = l.next
        else:
            curr.next = rest
            rest = rest.next
        curr = curr.next

    if not l is None or not rest is None:
        curr.next = l if l else rest

    return dummy.next


#l = ll_generate_ascending_list(10, 1)

#prev = None
#curr = l
#while curr:
#    tmp = curr.next
#    curr.next = prev

#    prev = curr
#    curr = tmp

#l = prev

#print l
#print sort_list(l)

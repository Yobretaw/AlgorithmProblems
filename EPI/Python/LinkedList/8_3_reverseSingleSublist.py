import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function which takes a singly linked list L and two integers s and f as arguments,
    and reverse the order of the nodes from the s-th node to f-th node, inclusive. The numbering
    begins at 1, i.e., the head node is the first node. Perform the reversal in a single pass.
    Do not allocate additional nodes.
    ============================================================================================
"""
def reverse_partial(l, s, f):
    if not l:
        return None

    if s == f:
        return l

    dummy = Node("*", l)
    prev = dummy
    count = 1
    while count < s:
        count += 1
        prev = prev.next
    
    tail = prev.next
    while count < f:
        tmp = tail.next
        tail.next = tmp.next

        # link parts together
        tmp.next = prev.next
        prev.next = tmp

        count += 1

    return dummy.next


l = ll_generate_ascending_list(10, 1)
#print reverse_partial(l.clone(), 1, 9)
#print reverse_partial(l.clone(), 1, 10)
print reverse_partial(l.clone(), 2, 5)

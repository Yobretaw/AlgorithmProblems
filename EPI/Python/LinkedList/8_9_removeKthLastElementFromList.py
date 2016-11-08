import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Given a singly lnked list and an integer k, write a function to remove the k-th last element
    from the list. Your algorithm cannot use more than a few words of storge, regardless of the
    length of the list. In particular, you cannot assume that it is possible to record the length
    of the list
    ============================================================================================
"""
def remove_k_last_node(l, k):
    dummy = Node('*', l)
    fast = dummy
    slow = dummy

    i = 0
    while i <= k:
        fast = fast.next
        i += 1

    while fast:
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next
    return dummy.next


l = ll_generate_ascending_list(10, 1)

print remove_k_last_node(l.clone(), 1)
print remove_k_last_node(l.clone(), 2)
print remove_k_last_node(l.clone(), 3)
print remove_k_last_node(l.clone(), 4)
print remove_k_last_node(l.clone(), 5)
print remove_k_last_node(l.clone(), 6)
print remove_k_last_node(l.clone(), 7)
print remove_k_last_node(l.clone(), 8)
print remove_k_last_node(l.clone(), 9)
print remove_k_last_node(l.clone(), 10)

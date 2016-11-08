import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function which takes as input a singly linked list L, and a nonnegative integer k,
    and reverse the list k nodes at a time. If the number of nodes n in the list is not a multiple
    of k, leave the last n mod k nodes unchanged. do not change the data stored within a node.
    ============================================================================================
"""
def reverse_k_nodes(l, k):
    if not l:
        return None

    if k < 2:
        return l

    dummy = Node('*', l)
    prev = dummy
    tail = dummy.next

    while True:
        # first check if the number ramaining nodes are greater than ore equal to k
        # if not, return dummy.next as we keep the last n mod k nodes unchanged
        rest = tail
        i = 0
        while i < k:
            if not rest:
                return dummy.next
            rest = rest.next
            i += 1

        # reverse the sublist with size k
        i = 1
        while i < k:
            tmp = tail.next
            tail.next = tmp.next

            tmp.next = prev.next
            prev.next = tmp

            i += 1

        prev = tail
        tail = tail.next

    return dummy.next


l = ll_generate_ascending_list(10, 1)
print reverse_k_nodes(l.clone(), 4)

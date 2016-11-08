import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    A posting list is a singly linked list with an addition "jump" field each node. The jump
    field points to any other node.

    Implement a function which takes a posting list and returns a copy of it. You can modify
    the original list, but must restore it to its initial state before returning.
    ============================================================================================
"""
def copy_posting_list(l):
    if not l or not l.next:
        return None if not l else Node(l.val, None)

    # first we construct a list that is interleaving with the original list:
    #
    # 1 -> 2 -> 3 -> 4 -> 5     ==>    1 -> _1 -> _2 -> _2 -> 3 -> _3 -> 4 -> _4 -> 5 -> _5
    curr = l
    while curr:
        tmp = curr.next
        curr.next = Node(curr.val, tmp)
        curr = curr.next.next

    # then we copy random pointer of each node
    curr = l
    while curr:
        curr.next.random = curr.random.next
        curr = curr.next.next

    # last we reverse the original list
    dummy = Node('*')
    prev = dummy
    curr = l
    while curr:
        prev.next = curr.next
        prev = prev.next

        curr.next = prev.next
        curr = curr.next

    return dummy.next


l = ll_generate_ascending_list(10, 1)
print copy_posting_list(l)

import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Given a linear nonrecursive function that reverses a singly linked list. The function should
    use no more than constant storge beyond that needed for the list itself.
    ============================================================================================
"""
def reverse(l):
    if not l:
        return

    prev = None
    curr = l

    while curr:
        tmp = curr.next

        curr.next = prev
        prev = curr

        curr = tmp

    return prev


l = ll_generate_ascending_list(10)

print l
print reverse(l)

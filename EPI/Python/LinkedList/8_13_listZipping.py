import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Let l be a singly linked list. Assume its nodes are numbered startin at 0. Define the zip of 
    l to be the list consisting of the interleaving of the nodes numbered 0, 1, 2,..., with the
    nodes numbered n - 1, n - 2, n - 3, ..., where n is the number of nodes in the list.

    l -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

                |  zipping
                v

    l -> 1 -> 6 -> 2 -> 5 -> 3 -> 4
    ============================================================================================
"""
def zip_list(l):
    if not l or not l.next or not l.next.next:
        return

    slow = l
    fast = l.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # reverse rest
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
        tmp = curr.next
        curr.next = prev

        prev = curr
        curr = tmp

    first = l
    second = prev
    while first and second:
        tmp = first.next
        tmp2 = second.next

        first.next, second.next = second, tmp

        first = tmp
        second = tmp2


#l = ll_generate_ascending_list(9, 1)
l = ll_generate_ascending_list(10, 1)
zip_list(l)
print l

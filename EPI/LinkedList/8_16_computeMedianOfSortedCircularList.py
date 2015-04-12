import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function that takes a pointer to an arbitrary node in a sorted circular linked list,
    and returns the median of the linked list.
    ============================================================================================
"""
def find_median(l):
    if not l or not l.next:
        return None if not l else l.val

    min_node = None
    n = 1
    curr = l.next
    while not curr is l:
        if curr.val > curr.next.val:
            min_node = curr.next

        n += 1
        curr = curr.next

    i = 1
    curr = min_node
    while i < n / 2:
        curr = curr.next
        i += 1

    if n & 1:
        return curr.val
    else:
        return (curr.val + curr.next.val) / 2.0

#l = ll_generate_ascending_list(9, 1)
#l = ll_generate_ascending_list(10, 1)

#end = l
#while end.next:
#    end = end.next

#end.next = l
#print find_median(l)

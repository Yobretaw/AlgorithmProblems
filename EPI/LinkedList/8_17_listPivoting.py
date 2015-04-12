import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    For any integer k, the pivot of a list of integers with respect to k is that list with its
    nodes reordered so that all nodes containing keys less than k appear before nodes containing
    k, and all nodes containing keys greater than k appear after the nodes containing k.

    Implement a function which takes as input a singly linked list and an integer k and performs
    a pivot of the list with respect to k. The relative order of nodes that appear before k, and
    after k, must remain unchanged; the same must hold for nodes holding keys equal to k.
    ============================================================================================
"""
def list_pivot(l, k):
    if not l:
        return

    less = Node('*')
    equal = Node('*')
    greater = Node('*')

    less_head = less
    equal_head = equal
    greater_head = greater

    curr = l
    while curr:
        if curr.val < k:
            less.next = curr
            less = less.next
        elif curr.val == k:
            equal.next = curr
            equal = equal.next
        else:
            greater.next = curr
            greater = greater.next

        curr = curr.next

    less.next = equal.next = greater.next = None

    if not equal_head.next:
        less.next = greater_head.next
    else:
        less.next = equal_head.next
        equal.next = greater_head.next

    return less_head.next


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
#print list_pivot(l, 4)

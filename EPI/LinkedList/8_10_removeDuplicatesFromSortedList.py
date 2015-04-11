import sys
import os
import math

merge = __import__('8_1_mergeTwoSortedList').merge

from linkedlist import *

"""
    ============================================================================================
    Write a function that takes as input singly linked list l of n integers in sorted order, and
    remove duplicates from it. The list should be sorted. Your may perform the change on L itself.
    ============================================================================================
"""
def remove_duplicates(l):
    if not l:
        return

    curr = l
    while curr:
        rest = curr.next
        while rest and curr.val == rest.val:
            rest = rest.next

        curr.next = rest
        curr = curr.next

#g = merge(ll_generate_ascending_list(10, 1), ll_generate_ascending_list(10, 10))
#print g
#remove_duplicates(g)
#print g


"""
    Variant 8.10.1: Let m be a positive integer and l a sorted singly linked list of integers.
    For each integer k, if k appears more than m times in l, remove all nodes from l containing k
"""
def remove_duplicates2(l, m):
    if not l:
        return None

    dummy = Node('*', l)
    prev = dummy
    curr = dummy.next

    while curr:
        i = 1
        rest = curr.next
        pre_rest = curr
        while rest and curr.val == rest.val:
            rest = rest.next
            pre_rest = pre_rest.next
            i += 1

        if i <= m:
            prev = pre_rest
        else:
            prev.next = rest

        curr = rest
    
    return dummy.next

#l = ll_generate_ascending_list(10, 1)
#f = ll_generate_ascending_list(10, 5)
#g = ll_generate_ascending_list(10, 7)
#h = merge(l, merge(f, g))

#print h
#print remove_duplicates2(h.clone(), 0)
#print remove_duplicates2(h.clone(), 1)
#print remove_duplicates2(h.clone(), 2)
#print remove_duplicates2(h.clone(), 3)

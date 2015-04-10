import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function that takes two sorted list l and f, and returns the merge of l and f. Your
    code should reuse the nodes from the lists provided as input. Your function should use O(1)
    additional space. The only field you can change in a node is 'next'.
    ============================================================================================
"""
def merge(l, f):
    if not l or not f:
        return l if l else f

    res = None
    if l.val < f.val:
        res, l = l, l.next
    else:
        res, f = f, f.next

    head = res

    while l and f:
        if l.val < f.val:
            res.next, l = l, l.next
        else:
            res.next, f = f, f.next

        res = res.next

    if l or f:
        res.next = l if l else f

    return head

#l = ll_generate_ascending_list(10, 0)
#f = ll_generate_ascending_list(10, 0)
#print merge(l, f)

"""
    Variant 8.1.1: Solve the same problem when the lists are doubly linked.
"""
def merge_double(l, f):
    if not l or not f:
        return l if l else f

    res = None
    if l.val < f.val:
        res, l = l, l.next
    else:
        res, f = f, f.next

    head = res
    while l and f:
        if l.val < f.val:
            l.prev, res.next, l = res, l, l.next
        else:
            f.prev, res.next, f = res, f, f.next
        
        res = res.next

    if l:
        l.prev, res.next = res, l
    elif f:
        f.prev, res.next = res, f

    return head


#l = ll_generate_ascending_list(10, 0)
#f = ll_generate_ascending_list(10, 0)
#res = merge_double(l, f)

#last = res

#while last.next:
#    last = last.next

#while last.prev:
#    print last.val
#    last = last.prev

#print last.val

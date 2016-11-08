import sys
import os
import math

from linkedlist import *
detect_cycle = __import__('8_5_testForCyclicity').detect_cycle
detect_overlap = __import__('8_6_testForOverlappingLists').detect_overlap

"""
    ============================================================================================
    Let l1 and l2 be cycle-free singly linked lists. Write a function that returns the first node
    that is shared by both lists. If no such node exists, return None.

    Note l and f may each or both have a cycle. If such a node exists, return a node that appears
    first when traversing the lists. This node may not be unique - if l ends in a cycle, the
    first node encountered when traversing l may be different from the first node encountered
    when traversing f, even though the cycle is the same.
    ============================================================================================
"""
def detect_overlap_with_cycle(l, f):
    if not l or not f:
        return None
    a = detect_cycle(l)
    b = detect_cycle(f)

    # none of them has cycle
    if not a and not b:
        return detect_overlap(l, f)

    
    if a is None or b is None:
        return None

    # both of them have cycles
    len_l = 0
    len_f = 0
    tmp_l = l
    tmp_f = f
    while not tmp_l is a:
        tmp_l = tmp_l.next
        len_l += 1

    while not tmp_f is b:
        tmp_f = tmp_f.next
        len_f += 1

    if len_l > len_f:
        l, f, a, b, len_l, len_f = f, l, b, a, len_f, len_l

    diff = len_f - len_l
    i = 0
    while i < diff:
        f = f.next
        i += 1

    while not l is a and not f is b:
        if l is f:
            break

        l, f = l.next, f.next

    return l

#l = ll_generate_ascending_list(10, 1)
#f = ll_generate_ascending_list(5, 10)

#a = l
#b = f

#while b.next:
#    b = b.next
#    a = a.next

#b.next = a.next

#a.next.next.next = b.next

#print detect_overlap_with_cycle(l, f).val

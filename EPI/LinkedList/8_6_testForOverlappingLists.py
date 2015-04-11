import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Let l1 and l2 be cycle-free singly linked lists. Write a function that returns the first node
    that is shared by both lists. If no such node exists, return None
    ============================================================================================
"""
def detect_overlap(l, f):
    if not l or not f:
        return False

    a = l
    b = f
    len_l = 0
    len_f = 0
    while a or b:
        len_l += 1 if a else 0
        len_f += 1 if b else 0

        a = a.next if a else None
        b = b.next if b else None

    if len_l > len_f:
        l, f = f, l
        len_l, len_f = len_f, len_l

    diff = len_f - len_l
    while diff:
        f = f.next
        diff -= 1

    while l and f and not l is f:
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

#print detect_overlap(l, f)

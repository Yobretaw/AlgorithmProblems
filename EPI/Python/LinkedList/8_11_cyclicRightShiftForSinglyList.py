import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function that takes as input a singly linked list and a nonnegative integer k, and
    returns the list cyclically shifted to the right by k.
    ============================================================================================
"""
def cyclic_right_shift(l, k):
    if not l or not k:
        return l

    n = l.length()
    k %= n

    if k == 0:
        return l

    curr = l
    diff = n - 1 - k
    while diff:
        curr = curr.next
        diff -= 1

    end = curr
    while end.next:
        end = end.next

    rest = curr.next
    curr.next = None
    end.next = l
    return rest

#l = ll_generate_ascending_list(10, 1)
#for i in range(1, l.length() + 1):
#    print cyclic_right_shift(l.clone(), i)

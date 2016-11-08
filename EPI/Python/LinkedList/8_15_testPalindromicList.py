import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function that test whether a singly linked list is palindomic
    ============================================================================================
"""
def is_palindromic(l):
    if not l or not l.next:
        return True

    slow = l
    fast = l.next

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # reverse the second half of l
    reverse(slow.next, slow)

    curr = slow.next
    while l and curr:
        if not l.val == curr.val:
            return False

        l, curr = l.next, curr.next

    # reverse back
    reverse(slow.next, slow)
    return True


def reverse(l, before):
    prev = None
    curr = l
    while curr:
        if before:
            before.next = curr
        
        tmp = curr.next
        curr.next = prev

        prev = curr
        curr = tmp


#l = ll_generate_ascending_list(10, 1)

#end = l
#while end.next:
#    end = end.next

#reverse(ll_generate_ascending_list(10, 1), end)
#print l
#print is_palindromic(l)

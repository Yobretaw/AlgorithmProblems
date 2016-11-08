import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    A singly linked list whose nodes contain digits can be viewed as an integer, with the least
    significant digit coming first. Such a representation can be used to represent unbounded integers.

        3 -> 1 -> 4  +  7 -> 0 -> 9      =      0 -> 2 -> 3 -> 1
    
    Write a function which takes two singly linked list of digits, and returns the list corresponding
    to the sum of the integers they represent. The least significant digit comes first.
    ============================================================================================
"""
def sum_list(l, f):
    if not l or not f:
        return l if l else f

    carry = 0
    head = Node('*')
    curr = head
    while l and f:
        val = l.val + f.val + carry

        carry = val / 10
        curr.next = Node(val % 10)
        curr = curr.next

        l, f = l.next, f.next

    if not l is None or not f is None:
        rest = l if l else f
        while rest:
            val = rest.val + carry
            carry /= 10
            curr.next = Node(val % 10)
            curr = curr.next

            rest = rest.next
    else:
        if carry > 0:
            curr.next = Node(carry)

    return head.next


l = ll_generate_ascending_list(5, 4)
f = ll_generate_ascending_list(3, 5)

print l
print f
print sum_list(l, f)


"""
    Variant 8.19.1: Solve the same problem when integers are represented as lists of digits
    with the most significant digit comes first.
"""
def sum_list_reverse(l, f):
    """
        We can first reverse both l and f, then pass reversed list to the above function, then 
        reverse the result as well as both l and f.
    """
    pass

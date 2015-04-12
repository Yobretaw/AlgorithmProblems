import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Let l be a linked list. Assume its nodes are numbered starting at 0. Define the even-odd merge
    of l to be the list consisting of even-numbered nodes followed by the odd-numbered nodes. The
    even-odd merge is illustrated in Figure 8.10

    Write a function that computes the even-odd merge.
    ============================================================================================
"""
def even_odd_merge(l):
    if not l:
        return

    odd_head = Node('*', l)
    odd_curr = odd_head
    even_curr = l

    while True:
        odd_curr.next = even_curr.next
        odd_curr = odd_curr.next

        if odd_curr and odd_curr.next:
            even_curr.next = odd_curr.next
            even_curr = even_curr.next
        else:
            even_curr.next = odd_head.next
            return

#l = ll_generate_ascending_list(1, 1)
#l = ll_generate_ascending_list(2, 1)
#l = ll_generate_ascending_list(3, 1)
#l = ll_generate_ascending_list(10, 1)
#even_odd_merge(l)
#print l

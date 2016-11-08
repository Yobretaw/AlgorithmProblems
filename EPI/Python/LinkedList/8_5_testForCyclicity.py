import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Given a reference to the head of a singly linked list, write a function that determines
    whether the list ends in a null or reaches a cycle of nodes. The function should return null
    if there does not exist a cycle, and the reference to the start of the cycle if a cycle is
    present.(You do not know the length of the list in advance)
    ============================================================================================
"""
def detect_cycle(l):
    if not l or not l.next:
        return None

    slow = l
    fast = l.next.next

    while True:
        if not fast or not fast.next:
            return None

        if fast == slow:
            break

        fast = fast.next.next
        slow = slow.next

    # now we know there exists a cycle, we then find its length
    c = 1
    curr = slow.next
    while not curr is slow:
        curr = curr.next
        c += 1

    # now we have the length of the cycle. Next we put two nodes, one at the begining
    # the list, the other is c nodes ahead of the previous one, we then interating both
    # of them. When they meet, that node is the start of the cycle.
    a = l
    b = l
    i = 0
    while i < c:
        b = b.next
        i += 1

    while not a is b:
        a = a.next
        b = b.next

    return a

#l = ll_generate_ascending_list(10, 1)

#mid = l
#last = l

#count = 0
#while count < 5:
#    mid = mid.next
#    count += 1

#while last.next:
#    last = last.next

#last.next = mid
#print detect_cycle(l).val

import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Reverse a linked list from position m to n. Do it in-place and in one-pass.

    For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,

    return 1->4->3->2->5->NULL.

    Note:
    Given m, n satisfy the following condition:
    1 <= m <= n <= length of list.
"""
def reverse_list(head, m, n):
        if not head or not head.next or m == n:
            return head

        dummy = Node('*')
        dummy.next = head

        prev = dummy
        tail = dummy
        i = j = 0
        while i < m - 1:
            prev = prev.next
            i += 1
        while j < n:
            tail = tail.next
            j += 1

        rest = tail.next
        start = prev.next
        while m <= n:
            tmp = start.next
            start.next = rest
            rest = start
            start = tmp
            n -= 1

        prev.next = tail
        return dummy.next

#l = ll_generate_ascending_list(10, 1)
#print reverse_list(l, 2, 4)

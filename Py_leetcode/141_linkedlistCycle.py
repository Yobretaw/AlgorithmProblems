import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a linked list, determine if it has a cycle in it.

    Follow up:
    Can you solve it without using extra space?
"""
def has_cycle(head):
    if not head or not head.next:
        return False

    fast = head
    slow = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    
    return False

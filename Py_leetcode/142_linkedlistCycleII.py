import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

    Follow up:
    Can you solve it without using extra space?
"""
def detect_cycle(head):
    if not head or not head.next:
        return None

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break

    if not slow is fast:
        return None
    
    cycle_len = 1
    curr = slow.next
    while not curr is slow:
        curr = curr.next
        cycle_len += 1

    curr = head
    steps = 0
    while not curr is slow:
        curr = curr.next
        steps += 1

    steps -= cycle_len
    count = 0
    curr = head
    while count < steps:
        curr = curr.next
        count += 1

    while not curr is slow:
        curr, slow = curr.next, slow.next
    
    return curr

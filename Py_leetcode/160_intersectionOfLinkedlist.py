import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Write a program to find the node at which the intersection of two singly linked lists begins.


    For example, the following two linked lists:

        A:          a1 -> a2
                            ↘
                             c1 -> c2 -> c3
                            /          
        B:     b1 -> b2 -> b3

    begin to intersect at node c1.

    Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""
def get_intersection_node(a, b):
    if not a or not b:
        return None

    alen = blen = 0

    curr = a
    while curr:
        curr = curr.next
        alen += 1

    curr = b
    while curr:
        curr = curr.next
        blen += 1

    longer = a if alen > blen else b
    shorter = a if alen <= blen else b

    diff = abs(alen - blen)
    while diff:
        longer = longer.next
        diff -= 1

    while shorter and longer and not longer is shorter:
        shorter, longer = shorter.next, longer.next

    return longer

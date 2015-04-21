import sys
import math
import imp

#Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a linked list, remove the nth node from the end of list and return its head.

    For example,

       Given linked list: 1->2->3->4->5, and n = 2.

       After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    Given n will always be valid.
    Try to do this in one pass.
"""
def remove_from_end(l, k):
    """
        Remove kth node from the end of the given list l
    """
    dummy = Node('*', l)

    fast = dummy
    slow = dummy

    while k >= 0 and fast:
        fast = fast.next
        k -= 1
    
    if k > 0:
        return dummy.next

    while fast:
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next
    return dummy.next


#l = ll_generate_ascending_list(10)
#print l
#for i in range(0, 10):
    #print remove_from_end(l.clone(), i + 1)

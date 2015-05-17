import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    A linked list is given such that each node contains an additional random pointer
    which could point to any node in the list or null.

    Return a deep copy of the list.
"""
def copy_random_list(head):
    if not head:
        return None

    curr = head
    while curr:
        tmp = curr.next
        curr.next = Node(curr.val)
        curr.next.next = tmp
        curr = tmp

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    dummy = Node('*')
    prev = dummy
    curr = head
    while curr:
        prev.next = curr.next
        prev = prev.next
        curr.next = curr.next.next
        curr = curr.next
    return dummy.next


#l1 = Node(1)
#l2 = Node(2)
#l3 = Node(3)

#l1.next, l2.next = l2, l3
#l1.random, l2.random = l3, l1

#new = copy_random_list(l1)
#print new.random
#print new.next.random

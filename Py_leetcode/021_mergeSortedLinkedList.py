import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""
def merge(l, f):
    if not l or not f:
        return l if l else f

    dummy = Node('*')
    prev = dummy
    
    while l and f:
        if l.val < f.val:
            prev.next = l
            l = l.next
        else:
            prev.next = f
            f = f.next

        prev = prev.next

    if l or f:
        prev.next = l if l else f

    return dummy.next

#l = ll_generate_ascending_list(10, 1)
#f = ll_generate_ascending_list(10, 1)

#print merge(l, f)

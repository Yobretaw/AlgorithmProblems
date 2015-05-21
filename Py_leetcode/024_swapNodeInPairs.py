import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a linked list, swap every two adjacent nodes and return its head.

    For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.

    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
def swap_nodes_in_pairs(head):
        if not head or not head.next:
            return head

        dummy = Node('*')
        dummy.next = head

        prev = dummy
        curr = prev.next

        while curr and curr.next:
            tmp = curr.next.next
            prev.next = curr.next
            curr.next = tmp
            prev.next.next = curr
            curr = tmp
            prev = prev.next.next

        return dummy.next

l = ll_generate_ascending_list(10, 1)
print swap_nodes_in_pairs(l)

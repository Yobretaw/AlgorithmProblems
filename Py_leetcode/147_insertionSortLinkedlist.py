import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Sort a linked list using insertion sort.
"""
def insertion_sort(head):
    if not head or not head.next:
        return head

    new_head = head
    head = head.next
    new_head.next = None
    while head:
        next_node = head.next
        curr = new_head
        prev = None
        while curr and head.val > curr.val:
            prev = prev.next if prev else curr
            curr = curr.next

        if not prev:
            tmp = new_head
            new_head = head
            new_head.next = tmp
        else:
            prev.next = head
            prev.next.next = curr
        head = next_node

    return new_head

#l = Node(3, Node(4, Node(2, Node(1, Node(8)))))
#print insertion_sort(l)

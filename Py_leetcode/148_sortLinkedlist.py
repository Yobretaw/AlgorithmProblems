import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Sort a linked list in O(n log n) time using constant space complexity.
"""
def sort_list(head):
    if not head or not head.next:
        return head

    premid = None
    mid = head
    end = head
    while end and end.next:
        premid = premid.next if premid else mid
        mid, end = mid.next, end.next.next

    if end:
        premid, mid = premid.next, mid.next

    premid.next = None

    left = sort_list(head)
    right = sort_list(mid)

    if left.val < right.val:
        head = left
        left = left.next
    else:
        head = right
        right = right.next

    prev = head
    while left and right:
        if left.val < right.val:
            prev.next = left
            left = left.next
        else:
            prev.next = right
            right = right.next
        prev = prev.next

    if left or right:
        prev.next = left if left else right

    return head

#l = Node(3, Node(4, Node(2, Node(1, Node(8)))))
#print sort_list(l)

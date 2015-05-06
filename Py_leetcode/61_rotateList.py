import sys
import os
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a list, rotate the list to the right by k places, where k is non-negative.

    For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
"""
def rotate_list(l, k):
    if not head:
        return head

    k %= get_len(head)
    if k < 1:
        return head
        
    dummy = ListNode('-')
    dummy.next = head
    fast = dummy
    slow = dummy
    while k > 0:
        fast = fast.next
        k -= 1
    while fast.next:
        fast, slow = fast.next, slow.next
    
    new_head = slow.next
    slow.next = None
    end = new_head
    while end.next:
        end = end.next
    end.next = head
    return new_head
    

def get_len(l):
    count = 0
    while l:
        l = l.next
        count += 1
    return count


#def rotate_list_by_k_size(l, k):
#    if not l or not l.next or k < 2:
#        return l
    
#    dummy = Node('-')
#    dummy.next = l
#    before = dummy
#    curr = before.next
#    while has_next(curr, k)[0]:
#        count = 0
#        prev = has_next(curr, k)[1]
#        tail = curr
#        while count < k:
#            tmp = curr.next
#            curr.next = prev
#            prev = curr
#            curr = tmp
#            count += 1
#        before.next = prev
#        before = tail
#    return dummy.next

#def has_next(l, k):
#    tail = None
#    while l and k:
#        tail = l
#        l = l.next
#        k -= 1
#    return (k == 0, l)

#l = ll_generate_ascending_list(10)
#for i in range(0, 10):
#    print rotate_list_by_k_size(l.clone(), i + 1)

import sys
import math
import random
import itertools

ListNode = imp.load_source('ListNode', '../LinkedList/linkedlist.py').Node

"""
    Implement a routine which sorts lists efficiently. It should be a stable
    sort, i.e., the relative positions of equal elements must remain unchanged.
"""
def stable_sort(l):
    n = len(l)
    if n < 2:
        return l

    return merge_sort(l)

def merge_sort(l):
    n = len(l)
    if n < 2:
        return l

    mid = n / 2
    first, second = merge_sort(l[:mid]), merge_sort(l[mid:])
    write_idx = 0
    i = j = 0
    while i < len(first) or j < len(second):
        a = first[i] if i < len(first) else sys.maxint
        b = second[j] if j < len(second) else sys.maxint

        if a <= b:
            l[write_idx] = a
            i += 1
        else:
            l[write_idx] = b
            j += 1
        write_idx += 1

    return l

def merge_sort_linked_list(l):
    if not l or not l.next:
        return l

    pre_slow = ListNode('', l)
    slow = fast = l
    while fast and fast.next:
        pre_slow = pre_slow.next
        slow = slow.next
        fast = fast.next.next

    pre_slow.next = None
    first, second = merge_sort_linked_list(l), merge_sort_linked_list(slow)

    head = LinkedList('', l)
    prev = head
    while first and second:
        if first.val <= second.val:
            prev.next = first
            first = first.next
        else:
            prev.next = second
            second = second.next
        prev = prev.next

    if first or second:
        prev.next = first if first else second

    return head.next



if __name__ == '__main__':
    l = random.sample(range(100), 100)
    print l
    print stable_sort(l)

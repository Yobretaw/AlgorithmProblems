import sys
import os
import math

class Node():
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        arr = []
        arr.append(self.val)

        head = self.next
        while head:
            arr.append(head.val)
            head = head.next

        return ', '.join([str(val) for val in arr])

    def get_length(self):
        l = 1
        head = self.next
        while head:
            l += 1
            head = head.next

        return l

    def clone(self):
        head = Node(self.val)

        curr = self.next
        tmp = head

        while curr:
            tmp.next = Node(curr.val)
            curr = curr.next
            tmp = tmp.next

        return head


def ll_generate_ascending_list(n, start=0):
    nodes = [Node(i + start) for i in range(0, n)]

    for i in range(0, n - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]


def ll_is_same(l, f):
    while l and f:
        if l.val != f.val:
            return False

        l, f = l.next, f.next

    if l or f:
        return False

    return True

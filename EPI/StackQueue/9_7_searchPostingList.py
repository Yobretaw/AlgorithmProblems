import sys
import os
import math
import imp

from stack import Stack

LinkedList = imp.load_source('Node', '../LinkedList/linkedlist.py')
Node = LinkedList.Node
ll_generate_ascending_list = LinkedList.ll_generate_ascending_list

"""
    ============================================================================================
    Posting list are described in Problem 8.14. One way to enumerate the nodes in a posting list
    is to iteratively follow the next field. Another is to always first follow the jump field if
    it leads to a node that has not seen before, and then search from the next node. Call the
    order in which these nodes are traversed the jump-first order.

    Write recursive and iterative routines that takes a posting list, and computes the jump-first
    order. Assume each node has an order field, which is an integer that is initialized to -1 for
    each node.
    ============================================================================================
"""
def search_posting_list(l):
    """
        This function just print value of nodes in jump-first order. It doesn't modify values of nodes
    """
    if not l:
        return

    if not l.next:
        print l.val
        return

    s = Stack()
    m = {}

    curr = l
    while not s.empty() or curr:
        if not curr:
            curr = s.top()
            s.pop()
        elif curr in m:
            if s.empty():
                curr = None
            else:
                curr = s.top().next
                s.pop()
        else:
            m[curr] = 1
            print curr.val
            s.push(curr)
            curr = curr.random


def search_posting_list2(l):
    """
        This function assumes all nodes have initial value of -1, and it assigns order to each node
    """
    s = Stack()
    order = 1
    s.push(l)
    while not s.empty():
        curr = s.top()
        s.pop()
        if curr and curr.val == -1:
            curr.val = order
            order += 1
            s.push(curr.next)
            s.push(curr.random)
    

#n1 = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#n4 = Node(4)

#n1.next = n2
#n2.next = n3
#n3.next = n4

#n1.random = n3
#n2.random = n4
#n3.random = n1
#n4.random = n2

#search_posting_list(n1)


#n1 = Node(-1)
#n2 = Node(-1)
#n3 = Node(-1)
#n4 = Node(-1)

#n1.next = n2
#n2.next = n3
#n3.next = n4

#n1.random = n3
#n2.random = n4
#n3.random = n1
#n4.random = n2

#search_posting_list2(n1)
#print n1

import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

    You may not alter the values in the nodes, only nodes itself may be changed.

    Only constant memory is allowed.

    For example,
    Given this linked list: 1->2->3->4->5

    For k = 2, you should return: 2->1->4->3->5

    For k = 3, you should return: 3->2->1->4->5
"""
def reverse_nodes_k_group(head, k):
        if not head or k < 2:
            return head

        tail = head
        i = 1
        while tail.next and i < k:
            tail = tail.next
            i += 1

        if i < k:
            return head

        newHead = tail
        curr = head
        last = curr
        prev = tail.next
        while tail:
            i = 0
            while i < k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                tail = tail.next if tail else None
                i += 1

            last.next = tail
            last = curr if tail else last
            prev = tail.next if tail else None

        last.next = curr
        return newHead
        

#n = 10
#l = ll_generate_ascending_list(n, 1)
##print reverse_nodes_k_group(l.clone(), 2)
#for i in range(0, n):
#    print reverse_nodes_k_group(l.clone(), i + 1)

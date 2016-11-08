import sys
import os
import math
import imp

from BST import Node, bst_print
ListNode = imp.load_source('ListNode', '../LinkedList/linkedlist.py').Node
ll_generate_ascending_list = \
        imp.load_source('ListNode', '../LinkedList/linkedlist.py').ll_generate_ascending_list


"""
    Let L be a doubly linked list of numbers, sorted in nondecreasing order.
    Design an efficient algorithm that takes as input L, and builds a height-
    balanced BST on the entries in L. You cannot use dynamic memory allocation-
    reuse the nodes of L for the BST. You can use O(logn) additional memory
    implicitly on the function call stack. Use the 'prev' and 'next' fields for
    'left' and 'right' respectively.
"""
def convert_linked_list_to_bst(head):
    if not l:
        return None

    n = head.length()
    curr = [head]
    return convert_linked_list_to_bst_help(0, n, curr)

def convert_linked_list_to_bst_help(start, end, curr):
    if start == end:
        return None

    if start == end - 1:
        node = curr[0]
        curr[0] = curr[0].next if curr[0] else None
        node.prev = node.next = None
        return node

    mid = start + (end - start) / 2
    l = convert_linked_list_to_bst_help(start, mid, curr)

    root = curr[0]
    root.prev = l
    
    curr[0] = root.next
    root.next = convert_linked_list_to_bst_help(mid + 1, end, curr)

    return root

def print_double_linked_list_as_bst(root):
    output = []
    print_double_linked_list_as_bst_help(root, 0, output)

def print_double_linked_list_as_bst_help(root, level, output):
    if root:
        print_double_linked_list_as_bst_help(root.next, level + 1, output)
        val = root.val
        if val == None:
            val = 'N'
        print ' ' * 4 * level + str(val)
        print ' '
        print_double_linked_list_as_bst_help(root.prev, level + 1, output)

if __name__ == '__main__':
    l = ll_generate_ascending_list(15)
    root = convert_linked_list_to_bst(l)
    print_double_linked_list_as_bst(root)

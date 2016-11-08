import sys
import os
import imp
import math

from BST import Node, bst_print, generate_complete_bst

convert_bst_to_doubly_linked_list = imp.load_source('Convert', './15_12_convert_bst_to_sorted_linked_list.py').convert_bst_to_doubly_linked_list


"""
    Let A and B be BSTs. Design an algorithm that merges them in O(n) time,
    where n is the total number of nodes in the BSTs. You cannot use dynamic
    allocation. You do not need to preserve the original trees. You can update
    fields, but cannot change the key stored in a node.
"""
def merge_bsts(r1, r2):
    if not r1 or not r2:
        return r1 if not r2 else r2

    # fisrt convert trees into doubly linked lists
    l1 = convert_bst_to_doubly_linked_list(r1)
    l2 = convert_bst_to_doubly_linked_list(r2)

    l1.left = l2.left = None

    tmp1 = l1
    while tmp1.right != l1:
        tmp1 = tmp1.right
    tmp1.right = None

    tmp2 = l2
    while tmp2.right != l2:
        tmp2 = tmp2.right
    tmp2.right = None

    # we then merge two lists l1 and l2
    head = prev = None
    if l1.val < l2.val:
        head = prev = l1
        l1 = l1.right
    else:
        head = prev = l2
        l2 = l2.right

    while l1 and l2:
        if l1.val < l2.val:
            prev.right, l1 = l1, l1.right
        else:
            prev.right, l2 = l2, l2.right
        prev = prev.right

    if l1 or l2:
        prev.right = l1 if l1 else l2

    # now convert the merged linked list back to BST
    res = convert_linked_list_to_bst(head)
    return res

"""
    Same as 15.11, except for replacing '.next' to '.right'
"""
def convert_linked_list_to_bst(head):
    if not head:
        return None

    n = 1
    tmp = head
    while tmp.right:
        n += 1
        tmp = tmp.right

    curr = [head]
    return convert_linked_list_to_bst_help(0, n, curr)

def convert_linked_list_to_bst_help(start, end, curr):
    if start == end:
        return None

    if start == end - 1:
        node = curr[0]
        curr[0] = curr[0].right if curr[0] else None
        node.left = node.right = None
        return node

    mid = start + (end - start) / 2
    l = convert_linked_list_to_bst_help(start, mid, curr)

    root = curr[0]
    root.left = l
    
    curr[0] = root.right
    root.right = convert_linked_list_to_bst_help(mid + 1, end, curr)
    return root

if __name__ == '__main__':
    r1 = Node(1, Node(0), Node(1.5))
    r2 = Node(2, Node(1.75), Node(3))

    bst_print(merge_bsts(r1, r2))

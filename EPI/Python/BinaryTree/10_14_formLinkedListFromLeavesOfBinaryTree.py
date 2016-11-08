import sys
import os
import math
import imp

Node = imp.load_source('Node', '../BST/BST.py').Node
ListNode = imp.load_source('Node', '../LinkedList/linkedlist.py').Node
Stack = imp.load_source('Node', '../StackQueue/stack.py').Stack
bst_print = imp.load_source('Node', '../BST/BST.py').bst_print

"""
    Given a binary tree, compute a linked list from the leaves of the binary tree. The leaves
    should appear in left-to-right order.
"""
def leavesToLinkedList(root):
    if not root:
        return None

    dummy = ListNode('Dummy')
    leavesToLinkedListHelp(root, [dummy])
    return dummy.next

def leavesToLinkedListHelp(root, prev):
    if not root.left and not root.right:
        prev[0].next = ListNode(root.val)
        prev[0] = prev[0].next
        return

    leavesToLinkedListHelp(root.left, prev)
    leavesToLinkedListHelp(root.right, prev)

#root = Node(2, Node(1), Node(3))
#print leavesToLinkedList(root)

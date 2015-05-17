import sys
import math
import imp

Node = imp.load_source('Node', '../EPI/BST/BST.py').Node
bst_print = imp.load_source('Node', '../EPI/BST/BST.py').bst_print

"""
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers.

    For example,

        1
       / \
      2   3
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.

    Return the sum = 12 + 13 = 25.
"""
def sum_numbers(root):
    return sum_numbers_help(root, 0)

def sum_numbers_help(root, curr):
    if not root:
        return 0

    curr = 10 * curr + root.val
    if not root.left and not root.right:
        return curr
    return sum_numbers_help(root.left, curr) + sum_numbers_help(root.right, curr)

root = Node(1, Node(2), Node(3))
print sum_numbers(root)


import sys
import os
import imp
import math

from BST import Node, \
        bst_print, \
        generate_complete_bst, \
        bst_insert_node, \
        bst_remove_node, \
        bst_get_leftmost, \
        bst_get_rightmost

"""
    Suppose each node in a BST has a size field, which denotes the number of
    nodes at the subtree rooted at that node, inclusive of the node. How would
    you efficiently compute the nubmer of keys that lie in a given range? Can
    the size field be updated efficiently on insert and delete? Your solution
    should work in presence of duplicates keys.
"""
def count_node_in_range(root, lower, upper):
    if not root:
        return 0

    if root.val <= lower or root.val >= upper:
        return int(root.val == lower or root.val == upper) + \
                (count_node_in_range(root.right, lower, upper) \
                    if root.val < lower \
                    else count_node_in_range(root.left, lower, upper))

    count = 0
    if lower == -sys.maxint:
        count += root.left.size if root.left else 0
    elif root.val > lower and upper > root.val:
        count += count_node_in_range(root.left, lower, sys.maxint)

    if upper == sys.maxint:
        count += root.right.size if root.right else 0
    elif root.val < upper and lower < root.val:
        count += count_node_in_range(root.right, -sys.maxint, upper)

    return count + 1


if __name__ == '__main__':
    root = generate_complete_bst(15)
    bst_print(root, print_size=True)

    print count_node_in_range(root, 8, 8)
    print count_node_in_range(root, 8, 9)
    print count_node_in_range(root, 4, 9)
    print count_node_in_range(root, 4, 15)
    print count_node_in_range(root, -1, 15)

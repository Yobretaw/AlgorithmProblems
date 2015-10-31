import sys
import os
import math

from BST import Node, bst_print, generate_complete_bst, find_node


"""
    Let r, s and m be distinct nodes in a BST. In this BST, nodes do not have
    pointers to their parents and all keys are unique. Write a function which
    returns true if m has both an ancestor and a descendant in the set {r, s}.
"""
def test_total_order(root, r, s, m):
    if not root:
        return False

    ancestor = None
    while root:
        if root is r or root is s:
            ancestor = r if root is r else s
        elif root is m:
            break

        root = root.left if root.val > m.val else root.right

    if not ancestor:
        return False

    # now root is node m, traverse all its descendants to test node s
    descendant = r if ancestor is s else s
    while root:
        if root is descendant:
            return True

        root = root.left if root.val > descendant.val else root.right
    return False


if __name__ == '__main__':
    root = generate_complete_bst(127)
    bst_print(root)

    r, s, m = find_node(root, 22), find_node(root, 31), find_node(root, 23)
    print test_total_order(root, r, s, m) == True

    r, s, m = find_node(root, 15), find_node(root, 31), find_node(root, 23)
    print test_total_order(root, r, s, m) == False


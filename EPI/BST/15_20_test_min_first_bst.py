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
    A min-first BST is one in which the minimum key is stored at the root;
    each key in the left subtree is less than every key in the right subtree.
    The subtree themselves are min-first BSTs.

    Write a function that returns True if the given BST is a min-first BST,
    False otherwise.
"""
def test_min_first_bst(root):
    return test_min_first_bst_help(root)[0]

def test_min_first_bst_help(root):
    if not root:
        return True, None

    is_left_minfirst, left_max = test_min_first_bst_help(root.left)
    if not is_left_minfirst or root.left and root.left.val <= root.val:
        return False, None

    is_right_minfirst, right_max = test_min_first_bst_help(root.right)
    if not is_right_minfirst \
            or (root.right and left_max and root.right.val <= left_max):
        return False, None

    return True, max(left_max, root.val, right_max)


"""
    Variant 1:

    Write a function that takes a min-first BST T and key k, and returns True
    if and only if T contains k.
"""
def test_key_exists(root, k):
    if not root or root.val > k:
        return False

    if root.val == k:
        return True

    if root.right and root.right.val <= k:
        return test_key_exists(root.right, k)
    else:
        return test_key_exists(root.left, k)


"""
    Variant 2:

    Print the keys of in a min-first BST in sorted order.
"""
def print_min_first_bst(root):
    if not root:
        return

    print root.val
    print_min_first_bst(root.left)
    print_min_first_bst(root.right)


"""
    Variant 3:

    A max-first BST is defined analogouly to the min-first BST, the difference
    being that the largest key is stored at the root. Design an algorithm that
    transforms a min-first BST into a max-first BST. Use as little additional
    space as possible.
"""
def transform_min_first_bst(root):
    if not root:
        return None

    l = transform_min_first_bst(root.left)
    r = transform_min_first_bst(root.right)

    root.left = root.right = None

    if not l and not r:
        return root

    left_most_node = l if l else r
    while left_most_node.left:
        left_most_node = left_most_node.left

    left_most_node.left = root
    if not l or not r:
        return l if l else r

    parent = r
    while parent.left:
        parent = parent.left

    parent.left = l
    return r


if __name__ == '__main__':
    root = Node(2,
            Node(3,
                None,
                Node(5,
                    Node(7),
                    Node(11))),
            Node(13,
                Node(17),
                Node(19,
                    Node(23),
                    None)))
    # bst_print(root)
    print test_min_first_bst(root) == True

    root = Node(2,
            Node(3,
                None,
                Node(8,
                    Node(7),
                    Node(11))),
            Node(13,
                Node(17),
                Node(19,
                    Node(23),
                    None)))
    # bst_print(root)
    print test_min_first_bst(root) == False

    root = Node(2,
            Node(3,
                None,
                Node(5,
                    Node(7),
                    Node(11))),
            Node(13,
                Node(10),
                Node(19,
                    Node(23),
                    None)))
    # bst_print(root)
    print test_min_first_bst(root) == False

    root = Node(2,
            None,
            Node(13,
                Node(17),
                Node(19,
                    Node(23),
                    None)))
    # bst_print(root)
    print test_min_first_bst(root) == True

    root = Node(2,
            Node(3,
                None,
                Node(5,
                    Node(7),
                    Node(11))),
            Node(13,
                Node(17),
                Node(19,
                    Node(23),
                    None)))

    print test_key_exists(root, 3) == True
    print test_key_exists(root, 11) == True
    print test_key_exists(root, 12) == False
    print test_key_exists(root, 23) == True
    print test_key_exists(root, 11) == True

    print_min_first_bst(root)

    bst_print(transform_min_first_bst(root))

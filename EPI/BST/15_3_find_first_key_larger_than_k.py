import sys
import os
import math
from BST import Node


"""
    Write a function that takes a BST T and a key k, and returns the first
    entry larger than k that would appear in an inorder traversal. If k is
    absent or no key larger than k is present, return None.
"""
def find_first_key_larger_than_k(root, k):
    """
        Note this version of implementation assume k doesn't need to be a key
        in the tree
    """
    if not root:
        return None

    if root.val <= k:
        return find_first_key_larger_than_k(root.right, k)
    l = find_first_key_larger_than_k(root.left, k)
    if l:
        return l
    else:
        return root.val if root.val > k else None

def find_first_key_larger_than_k2(root, k):
    """
        Note this version of implementation will return None if k is not a key
        present in the tree.
    """
    if not root:
        return None

    return find_first_key_larger_than_k2_help(root, k, [False])

def find_first_key_larger_than_k2_help(root, k, seen):
    if not root:
        return None

    l = find_first_key_larger_than_k2_help(root.left, k, seen)
    if seen[0]:
        return root.val if not l else l
    elif root.val == k:
        seen[0] = True
    return find_first_key_larger_than_k2_help(root.right, k, seen)

def find_first_key_larger_than_k3(root, k):
    """
        Same assumption as find_first_key_larger_than_k2
    """
    found = False
    curr = root
    first = None

    while curr:
        if curr.val == k:
            found = True
            curr = curr.right
        elif curr.val > k:
            first = curr
            curr = curr.left
        else:
            curr = curr.right

    return first if found else None



if __name__ == '__main__':
    root = Node(19,
            Node(7,
                Node(3,
                    Node(2),
                    Node(5)),
                Node(11,
                    None,
                    Node(17,
                        Node(13),
                        None))),
            Node(43,
                Node(23,
                    None,
                    Node(37,
                        Node(29,
                            None,
                            Node(31)),
                        Node(41))),
                Node(53)))

    print find_first_key_larger_than_k(root, 23)
    print find_first_key_larger_than_k(root, 32)
    print find_first_key_larger_than_k(root, 51)
    print '-' * 100
    print find_first_key_larger_than_k2(root, 23)
    print find_first_key_larger_than_k2(root, 32)
    print find_first_key_larger_than_k2(root, 37)
    print find_first_key_larger_than_k2(root, 51)
    print '-' * 100
    print find_first_key_larger_than_k3(root, 23)
    print find_first_key_larger_than_k3(root, 32)
    print find_first_key_larger_than_k3(root, 37)
    print find_first_key_larger_than_k3(root, 51)

import sys
import os
import math
from BST import Node


"""
    Given a BST T, write recursive and iterative versions of a function that
    takes a BST T, a key k, and returns the node containing k that would appear
    first in an inorder traversal. If k is absent, return null.
"""
def find_first_occurence_recursive(root, k):
    if not root:
        return None

    l = find_first_occurence(root.left, k)
    if l:
        return l

    if root.val == k:
        return root

    r = find_first_occurence(root.right, k)
    return r


def find_first_occurence_iterative(root, k):
    if not root:
        return None

    curr = root
    while curr:
        if not curr.left:
            if curr.val == k:
                return curr
            curr = curr.right
        else:
            prev = root.left
            while prev.right and prev.right != curr:
                prev = prev.right
            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                if curr.val == k:
                    return curr
                curr = curr.right
    return None


if __name__ == '__main__':
    root = Node(1)
    print find_first_occurence_iterative(root, 0) is None
    print find_first_occurence_iterative(root, 1) is root
    print find_first_occurence_iterative(root, 2) is None


    root = Node(1, Node(0), Node(2))
    print find_first_occurence_iterative(root, 0) is root.left
    print find_first_occurence_iterative(root, 1) is root
    print find_first_occurence_iterative(root, 2) is root.right

    print find_first_occurence_iterative(root, 0) is root.left
    print find_first_occurence_iterative(root, 1) is root
    print find_first_occurence_iterative(root, 2) is root.right
    print find_first_occurence_iterative(root, 3) is None

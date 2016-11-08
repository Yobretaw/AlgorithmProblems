import sys
import os
import math
from BST import Node


"""
    Design an algorithm that takes a BST T of size n and height h, nodes s and
    b, and returns the LCA of s and b. Assume s.key < b.key. Your algorithm
    should run in O(h) time and O(1) space. Nodes do not have pointers to their
    parents.
"""
def compute_lca(root, a, b):
    if not root:
        return None

    if root is a or root is b:
        return root
    elif b.val < root.val:
        return compute_lca(root.left, a, b)
    elif a.val < root.val < b.val:
        return root
    else:
        return compute_lca(root.right, a, b)


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
                Node(47,
                    None,
                    Node(53))))

    a = root.left.left.left
    b = root.right.right.right
    print compute_lca(root, a, b) == root

    a = root.left.left.left
    b = root.left.right.right
    print compute_lca(root, a, b) == root.left

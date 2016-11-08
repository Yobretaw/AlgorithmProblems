import sys
import os
import math
from BST import Node, bst_node_count


"""
    Given the root of a BST and an integer k, design a function that finds the
    k largest elements in this BST.
"""
def find_k_largest_elements(root, k):
    if not k:
        return []

    res = []
    find_k_largest_elements_help(root, k, res)
    return res

def find_k_largest_elements_help(root, k, res):
    if not root:
        return

    find_k_largest_elements_help(root.right, k, res)

    if len(res) == k:
        return

    res.append(root.val)
    find_k_largest_elements_help(root.left, k, res)


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

    n = bst_node_count(root)
    for i in range(0, n + 1):
        print find_k_largest_elements(root, i)

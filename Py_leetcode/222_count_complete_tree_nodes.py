import sys
import heapq
from collections import defaultdict, deque


"""
    Given a complete binary tree, count the number of nodes.

    Definition of a complete binary tree from Wikipedia:

    In a complete binary tree every level, except possibly the last, is
    completely filled, and all nodes in the last level are as far left as
    possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
def count_complete_tree_nodes(root):
    if not root:
        return 0

    max_depth = compute_max_depth(root)
    start, end = 0, 1 << (max_depth - 1)
    while start != end - 1:
        mid = start + (end - start) / 2
        l = empty_at_level(root, mid, 1 << (max_depth - 2), max_depth)
        if l:
            start = mid
        else:
            end = mid

    return (2 ** (max_depth - 1)) - 1 + start + 1

def compute_max_depth(root):
    count = 0
    while root:
        root = root.left
        count += 1

    return count

def empty_at_level(root, idx, mid, remaining_depth):
    if remaining_depth == 1:
        return root is not None

    if idx < mid:
        mid -= (mid >> 1)
        return empty_at_level(root.left, idx, mid, remaining_depth - 1)
    else:
        mid += (mid >> 1)
        return empty_at_level(root.right, idx, mid, remaining_depth - 1)


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


if __name__ == '__main__':
    root = Node(2, Node(1))
    print count_complete_tree_nodes(root)
    root = Node(2, Node(1), Node(3))
    print count_complete_tree_nodes(root)
    root = Node(2, Node(1, Node(2), Node(3)), Node(3, Node(4)))
    print count_complete_tree_nodes(root)
    root = Node(2, Node(1, Node(2)), Node(3))
    root = Node(2, Node(1, Node(2), Node(3)), Node(3, Node(3), Node(3)))
    print count_complete_tree_nodes(root)

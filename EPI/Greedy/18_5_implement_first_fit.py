import sys
import math


"""
    Bin packing problem

    In the bin packing problem, objects of different volumes must be packed into
    a finite number of bins or containers each of volume V in a way that minimizes
    the number of bins used.

    Given a list of sizes of objects 'sizes', and the volume of containers V, use the
    first-fit algorithm to pack the given objects to contains.
"""
# ==================================================================================
#                               First Implementation
# 
# Return a list of set of sizes where each set represents items arranged in the same
# container
# ==================================================================================
def bin_pack_first_fit(sizes, V):
    if not sizes or not V:
        return []

    assert(V >= max(sizes))

    n = len(sizes)
    h = int(math.ceil(math.log(n, 2))) + 1

    root = build_complete_tree(h, V)
    for s in sizes:
        insert(root, s)

    res = []
    get_leaves(root, res)
    return res

def insert(root, val):
    if root.is_leaf_node():
        root.add_item(val)
        return True

    if root.left.is_leaf_node():
        if root.left.can_fit(val):
            insert(root.left, val)
        else:
            insert(root.right, val)

        max_remaining = root.left.max_size - min(root.left.total_size, root.right.total_size)
        root.size = max_remaining
        return max_remaining
    else:
        if root.left.size >= val:
            root.size = max(insert(root.left, val), root.right.size)
        else:
            root.size = max(insert(root.right, val), root.left.size)

def build_complete_tree(h, init_size):
    if h == 1:
        return LeafNode(init_size)

    root = Node(
            init_size,
            build_complete_tree(h - 1, init_size),
            build_complete_tree(h - 1, init_size)
    )
    return root

def get_leaves(root, res):
    if not root:
        return

    if root.is_leaf_node():
        if root.items:
            res.append(root.items)
        return

    get_leaves(root.left, res)
    get_leaves(root.right, res)

class Node:
    def __init__(self, size=None, left=None, right=None):
        self.size = size
        self.left = left
        self.right = right

    def is_leaf_node(self):
        return False

class LeafNode(Node):
    def __init__(self, max_size=0):
        self.items = set()
        self.total_size = 0

        self.max_size=max_size

    def add_item(self, item):
        self.items.add(item)
        self.total_size += item

    def can_fit(self, size):
        return self.max_size - self.total_size >= size

    def is_leaf_node(self):
        return True

# ==================================================================================
#                               Second Implementation
#
# Use a array to represent the complete tree
# ==================================================================================
class TreeNode:
    def __init__(self, cap=0):
        self.cap = cap
        self.items = set()

def bin_pack_first_fit2(sizes, V):
    if not sizes:
        return []

    assert(V >= max(sizes))

    n = len(sizes)
    nodes = [TreeNode(V) for i in range(2 * n - 1)]

    for val in sizes:
        i = 0
        path = []
        while 2 * i + 1 < len(nodes):
            path.append(i)
            idx = 2 * i + 1

            if nodes[idx].cap >= val:
                i = idx
            else:
                i = idx + 1

        nodes[i].cap -= val
        nodes[i].items.add(val)

        for idx in reversed(path):
            nodes[idx].cap = max(nodes[2 * idx + 1].cap, nodes[2 * idx + 2].cap)

    return [node.items for node in nodes if node.items]

if __name__ == '__main__':
    sizes = [3, 6, 2, 1, 5, 7, 2, 4, 1, 9]
    volume = 10
    print bin_pack_first_fit(sizes, volume)
    print bin_pack_first_fit2(sizes, volume)

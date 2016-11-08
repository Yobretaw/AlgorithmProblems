import sys
import math
import random


"""
    Design an algorithm for minimizing power that takes as input a rooted tree
    and assigns each node to a low or high voltage, subject to the design
    constraint that a low voltage node should never input to another low voltage
    node. Let c be the number of children of a node. The power used by a low
    voltage node is c + 1, while the power used by a high voltage node is 2(c + 1).

    Design an algorithm for minimizing power that takes as input a rooted tree and
    assigns each node to a low or high voltage, subject to the design constraint.

    ----

    Let l(r) and h(r) be the power comsumption of node r under low and high voltage,
    respectively. Let L(r) be the minimum possible power consumption that can be
    achieved when we assign a low voltage to r. Let H(r) be the minimum possible
    power consumption can be achieved when r is assigned a high voltage.

    Denote the set of all nodes that are inputs to r by I(r). Then the following
    recurrence relationships must hold for L and H.

                L(r) = l(r) + SUM_{c in I(r)}(H(c)),

                H(r) = h(r) + SUM_{c in I(r)}(min(L(c), H(c)))

    Using these equations, we can tabulate the values of L and H for all nodes.
    The desired solution is the minimum of the values of L and H for the root of
    the tree. Since we do a constant number of operations per node, the overall
    complexity is O(n), where n is then number of input nodes.
"""
def min_power_consumption(root):
    if not root:
        return 0
    
    f = {}
    return min(min_power_consumption_help(root, f))

# Return a tuple (low, high) where low represents L(r) and high represents H(r)
def min_power_consumption_help(root, f):
    if not root:
        return 0, 0

    if root in f:
        return f[root]

    num_children = count_children(root)
    l = min_power_consumption_help(root.left, f)
    r = min_power_consumption_help(root.right, f)

    low = num_children + 1 + l[1] + r[1]
    high = 2 * (num_children + 1) + min(l) + min(r)

    f[root] = (low, high)
    return f[root]

def count_children(root):
    return len(filter(None, [root.left, root.right]))


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    root = Node(None,
            Node(None,
                Node(None),
                Node(None)),
            Node(None))

    print min_power_consumption(root)

import sys
import os
import math
import imp
from collections import deque

"""
    Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


    OJ's undirected graph serialization:
    Nodes are labeled uniquely.

    We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
    As an example, consider the serialized graph {0,1,2#1,2#2,2}.

    The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
    Visually, the graph looks like the following:

           1
          / \
         /   \
        0 --- 2
             / \
             \_/
"""
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def clone_graph(node):
    seen = {}
    return clone_graph_help(node, seen)

def clone_graph_help(node, seen):
    if not node:
        return
    
    if node in seen:
        return seen[node]

    new_node = UndirectedGraphNode(node.val)
    seen[new_node] = node
    for n in node.neighbors:
        new_node.neighbors.append(clone_graph_help(n))
    return new_node

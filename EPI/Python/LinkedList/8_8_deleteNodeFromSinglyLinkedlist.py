import sys
import os
import math

from linkedlist import *

"""
    ============================================================================================
    Write a function which deletes a node in a singly linked list. The input node is guaranteed
    not to be the last node.
    ===========================================================================================
"""
def delete_node(l, d):
    """
        Assume value stored in each node is modifiable.
    """
    d.val = d.next.val
    d.next = d.next.next

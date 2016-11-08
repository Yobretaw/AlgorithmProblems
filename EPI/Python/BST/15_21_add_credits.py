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
    Design a data structure that implements the following methods:

        - insert(s, c), which adds client s with credit c, overwriting any
        existing entry for s.

        - remove(s), which removes client s

        - lookup(s), which returns the number of credits for each client, or -1
        if s is no present

        - addAll(c), the effect of which is to increment the number of credits
        for each client currently present by C.

        - max(), which returns any one client with the hightest number of
        credits.

    The insert(s, c), remove(s) and lookup(s) should run in time O(logn), where
    n is the number of credits. The remaining methods should run in time O(logn)
    Note s is of type string, and c is of type integer.

    ===========

    The idea is to use a balanced binary search tree and a hashmap to store
    client-credit relationships. The balanced BST is indexed by the credit,
    while the hashmap maps client string to the credit he owns.

    In order to do addAll() in O(1) time, we keey a global variable
    that recoreds the total increment to all clients' credit by far, and simply
    add that increment value to the return value of lookup().

    To do max() in O(1) time, we keep a record of the client with maximum credit
    everytime an insert() or remove() is called.
"""

import sys
import os
import math
import imp

from collections import defaultdict
from BST import Node

quick_select = imp.load_source('Select', '../Util/quick_select.py').select


"""
    This problem is a continuation of Problem 15.8. The difference is that only
    pages whose timestamp are within a specified duration of the page most
    recently read are to be considered.

    Implement the API in problem 15.8. If 'common' is called after processing
    the i-th entry, 'common' should return the k most visited pages whose
    timestamp is in [t_i - W, t_i], Here t_i is the timestamp of the i-th entry
    and W is specified by the client before any pages are read and does not
    change. RAM is limited - in particular you cannnot keep a map containing
    all pages. maximize time efficiency assuming calls to 'add' and 'common'
    may be interlaved and 'common' is frequently called.
"""

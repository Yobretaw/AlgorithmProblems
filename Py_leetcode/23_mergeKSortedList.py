import sys
import math
import imp
from operator import attrgetter

Node = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list
merge = imp.load_source('Node', './21_mergeSortedLinkedList.py').merge

"""
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
def merge_k_sorted_list(lists):
    n = len(lists)

    if n < 2:
        return lists[0] if n else None

    res = []
    i = 0
    while i + 1 < n:
        res.append(merge(lists[i], lists[i + 1]))
        i += 2

    if i == n - 1:
        res.append(lists[-1])
    
    return merge_k_sorted_list(res)


def merge_k_sorted_list2(lists):
        n = len(lists)

        if n < 2:
            return lists[0] if n else None

        res = []
        for l in lists:
            while l:
                res.append(l)
                l = l.next

        res = sorted(res, key=attrgetter('val'))
        for i, node in enumerate(res):
            try:
                node.next = res[i + 1]
            except:
                node.next = None

        return res[0] if res else None


#lists = []
#for i in range(0, 10):
#    lists.append(ll_generate_ascending_list(10, 10 * i + 1))

#print merge_k_sorted_list2(lists)

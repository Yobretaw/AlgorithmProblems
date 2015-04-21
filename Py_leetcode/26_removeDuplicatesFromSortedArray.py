import sys
import math
import imp

"""
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this in place with constant memory.

    For example,
    Given input array A = [1,1,2],

    Your function should return length = 2, and A is now [1,2].
"""
def remove_duplicates_from_array(A):
        if not A:
            return 0

        p = 1
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                A[p] = A[i]
                p += 1
        return p


#A = [1, 1, 2]
#print remove_duplicates_from_array(A)
#print A


#def remove_duplicates_linkedlist(l):
#        if not l or not l.next:
#            return 1 if l else 0

#        i = 0
#        curr = l
#        while curr:
#            next_node = curr.next
#            while next_node and next_node.val == curr.val:
#                next_node = next_node.next
#            curr.next = next_node
#            curr = curr.next
#            i += 1

#        return i

#l = ll_generate_ascending_list(10, 1)
#f = ll_generate_ascending_list(10, 1)

#m = merge(l, f)
#print m
#print remove_duplicates(m)

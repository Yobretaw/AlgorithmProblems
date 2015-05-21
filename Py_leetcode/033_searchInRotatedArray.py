import sys
import math

"""
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.
"""
def search_rotated_array(A, x):
    if not A:
        return -1

    start = 0
    end = len(A)
    while start < end:
        mid = start + (end - start) / 2
        if A[mid] == x:
            return mid

        """
        The interesting property of a sorted + rotated array is that when you divide it into two halves,
        atleast one of the two halves will always be sorted.

        We can easily know which half is sorted by comparing start and end element of each half.

        Once we find which half is sorted we can see if the key is present in that half - simple comparison with the extremes.

        If the key is present in that half we recursively call the function on that half 
        else we recursively call our search on the other half.
        """
        # left subarray is sorted
        if A[start] <= A[mid]:
            if A[start] <= x < A[mid]:
                end = mid
            else:
                # x < A[start] or x >= A[mid]
                start = mid + 1
        else:
            if A[mid] < x <= A[end - 1]:
                start = mid + 1
            else:
                # x <= A[mid] or x > A[end - 1]
                end = mid
    return -1


#A = [4, 5, 6, 7, 0, 1, 2]
#print search_rotated_array(A, 0)

#A = [3, 5, 1]
#print search_rotated_array(A, 3)
#print search_rotated_array(A, 5)
#print search_rotated_array(A, 1)

#A = [3, 1]
#print search_rotated_array(A, 1)

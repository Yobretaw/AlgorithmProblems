import sys
import os
import math

"""
    Given an array with n objects colored red, white or blue, sort them so that objects of
    the same color are adjacent, with the colors in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    Note:
    You are not suppose to use the library's sort function for this problem.

    click to show follow up.

    Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total
    number of 0's, then 1's and followed by 2's.

    Could you come up with an one-pass algorithm using only constant space?
"""
def sort_colors(arr):
    n = len(arr)
    if n < 2:
        return

    zero_end = 0
    unclassified = 0
    two_start = n
    while unclassified < two_start:
        if arr[unclassified] == 0:
            arr[zero_end] = 0
            if unclassified > zero_end:
                arr[unclassified] = 1
            zero_end += 1
            unclassified += 1
        elif arr[unclassified] == 1:
            arr[unclassified] = 1
            unclassified += 1
        else:
            arr[unclassified] = arr[two_start - 1]
            two_start -= 1
            arr[two_start] = 2

#arr = [2, 1, 0, 0, 1, 2]
#sort_colors(arr)
#print arr

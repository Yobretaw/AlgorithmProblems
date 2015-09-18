import sys
import os
import math
import random

"""
    Given an integer array, in which each entry but one appears in triplicate,
    with the remaining element appearing once, find the element appearing once.
    For example, if the array is [2, 4, 2, 5, 2, 5, 5], you should return 4
"""
def find_element_appear_once(arr):
    ones = twos = common_bit_mask = 0
    for v in arr:
        # The expression 'ones & v' gives the bits that are
        # there in both 'ones' and new element from arr[]. We add
        # these bits to 'twos' using bitwise OR
        twos |= ones & v

        # XOR the new bits with previous 'ones' to get all bits
        # appearing odd number of times
        ones ^= v

        # The common_bit_mask are those bits which appears third
        # times so they shouldn't appear in both 'ones' and 'twos'
        # common_bit_mask contains all these bits as 0, so that
        # these bits can be removed from 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)

        # Remove those bits that have appeared three times from
        # 'ones' and 'twos'
        ones &= common_bit_mask
        twos &= common_bit_mask

    return ones

#a = [2, 4, 2, 5, 2, 5, 5]
#print find_element_appear_once(a)

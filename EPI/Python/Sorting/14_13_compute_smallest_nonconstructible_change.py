import sys
import os
import math


"""
    Write a function which takes a array of positive integers and returns the
    smallest number which is not to the sum of a subset of elements of the
    array.
"""
def compute_smallest_change(nums):
    n = len(nums)
    if n < 2:
        return 1 if not n or nums[0] != 1 else 2

    nums.sort()
    total = 1
    for i in range(n):
        if nums[i] > total:
            break
        total += nums[i]
    return total


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 15, 10, 25]
    print compute_smallest_change(nums) == 5

    nums = [1, 2, 3, 4]
    print compute_smallest_change(nums) == 11

    nums = [1, 2, 2, 4]
    print compute_smallest_change(nums) == 10

    nums = [2, 3, 4, 5]
    print compute_smallest_change(nums) == 1

    nums = [1, 3, 2, 1]
    print compute_smallest_change(nums) == 8

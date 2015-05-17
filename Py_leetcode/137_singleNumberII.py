import sys
import math

"""
    Given an array of integers, every element appears three times except for one. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
def single_number(nums):
    n = len(nums)

    ones = twos = 0
    common_bit_maks = 0

    for i in  range(0, n):
        twos |= ones & nums[i]

        ones ^= nums[i]

        # equivalent as follows
        #common_bit_maks = ones & twos
        #ones ^= common_bit_maks
        #twos ^= common_bit_maks

        common_bit_maks = ~(ones & twos)
        
        ones &= common_bit_maks
        twos &= common_bit_maks

    return ones

def single_number_k(nums, k):
    res = 0
    for i in range(0, 32):
        count = 0
        for val in nums:
            if (val >> i) & 1:
                count += 1
        #res |= (count % k) << i
        # or..
        if count % 3:
            res |= 1 << i

    return res
    #return res - 2 ** 32 if res >= 2 ** 31 else res

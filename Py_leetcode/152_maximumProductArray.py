import sys
import os
import math

"""
    Find the contiguous subarray within an array (containing at least one number) which has the largest product.

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.
"""
def max_product(A):
    n = len(A)
    if n < 2:
        return A[0] if n else 0

    # the return value, always equals
    # to the maximum product of contiguous
    # subarray of A[0:i]
    res = A[0]

    # lastmax = max{ A[j]*A[j+1]*...*A[i] }, j=0:i
    # lastmin = min{ A[j]*A[j+1]*...*A[i] }, j=0:i
    lastmin = lastmax = A[0]

    for i in range(1, n):

        # new lastmax/lastmin can only obtained by
        # the element A[i] times old lastmax/lastmin
        # or the A[i] itself alone.
        a = A[i] * lastmax
        b = A[i] * lastmin

        lastmax = max(max(a, b), A[i])
        lastmin = min(min(a, b), A[i])
        
        res = max(res, lastmax)
    return res


def max_product2(A):
    n = len(A)
    if n < 2:
        return A[0] if n else 0
    
    res = -sys.maxint
    p = 1
    for i in range(0, n):
        p *= A[i]
        res = max(res, p)

        if A[i] == 0:
            p = 1

    p = 1
    for i in reversed(range(0, n)):
        p *= A[i]
        res = max(res, p)

        if A[i] == 0:
            p = 1

    return res


# AC'ed but too complicated..
#def max_product(nums):
#    n = len(nums)
#    if n < 2:
#        return nums[0] if n else 0

#    if not 0 in nums:
#        return max_product_help(nums, 0, n)
    
#    res = 0
#    start = 0
#    for end in range(0, n):
#        if nums[end] == 0:
#            res = max(res, max_product_help(nums, start, end))
#            start = end + 1
#    res = max(res, max_product_help(nums, start, n))
#    return res

    
#def max_product_help(nums, start, end):
#    if start == end - 1:
#        return nums[start]

#    neg_count = 0
#    neg_idx = []
#    for i in range(start, end):
#        if nums[i] < 0:
#            neg_count += 1
#            neg_idx.append(i)

#    if neg_count % 2 == 0:
#        return product_array(nums, start, end)

#    return max(product_array(nums, start, neg_idx[-1]), product_array(nums, neg_idx[0] + 1, end))

#def product_array(nums, start, end):
#    if start >= end:
#        return 0
#    res = 1
#    while start < end:
#        res *= nums[start]
#        start += 1
#    return res


nums = [2, -1, 3, 0, -2, 4]
nums = [0, 2]
nums = [-4, -3, -2]
nums = [0, -2, 0]
print max_product(nums)

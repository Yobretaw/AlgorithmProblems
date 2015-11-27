import sys
import math

"""
    Design an algorithm that takes as input an array A and a number t, and returns
    all subset of size 3 of the input array A that sums to t.
"""
def three_sum(nums, t=0):
    n = len(nums)
    if n < 3:
        return []

    nums.sort()
    res = []
    start = 0
    while start < n - 2:
        mid = start + 1
        end = n - 1

        while mid < end:
            val = [nums[start], nums[end], nums[mid]]
            if sum(val) == 0:
                res.append(val)
                mid += 1
                end -= 1
                while mid < end and nums[mid] == nums[mid - 1]:
                    mid += 1
                while mid < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif sum(val) > 0:
                end -= 1
            else:
                mid += 1

        while start < n - 2 and nums[start] == nums[start + 1]:
            start += 1
        start += 1
    return res


if __name__ == '__main__':
    A = [-2, 0, 1, 1, 2]
    t = 0
    print three_sum(A, t)

    A = [-1, 0, 1, 2, -1, -4]
    t = 0
    print three_sum(A, t)

    A = [12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1]
    t = 0
    for l in three_sum(A, t):
        print l

    print '-'* 100
    A = [10,-2,-12,3,-15,-12,2,-11,3,-12,9,12,0,-5,-4,-2,-7,-15,7,4,-5,-14,-15,-15,-4,10,9,-6,7,1,12,-6,14,-15,12,14,10,0,10,-10,3,4,-12,10,7,-9,-7,-15,-8,-15,-4,2,9,-4,3,-10,13,-3,-1,5,5,-4,-15,4,-11,4,-4,6,-11,-9,12,7,11,7,2,-5,13,10,-5,-10,3,7,0,-3,10,-12,2,9,-8,8,-9,13,12,13,-6,8,3,5,-9,7,12,10,-8,0,2,1,10,-7,-3,-10,-10,7,4,5,-11,-8,0,-2,-14,8,13,-8,-2,10,13]
    t = 0
    for l in three_sum(A, t):
        print l

import sys
from heapq import *


"""
    Given an integer array of size n, find all elements that appear more than
    n/3 times. The algorithm should run in linear time and in O(1) space.
"""
def find_majority_elements_II(nums):
        n = len(nums)
        q = []
        for v in nums:
            v_in_q = v in set(p[1] for p in q)
            if len(q) < 3 and not v_in_q:
                heappush(q, (1, v))
            elif v_in_q:
                q = [(p if p[1] != v else (p[0] + 1, v)) for p in q]
                heapify(q)
            else:
                q = [(p[0] - 1, p[1]) for p in q]
                while q and q[0][0] <= 0:
                    heappop(q)
        return [p[1] for p in q if nums.count(p[1]) * 3 > n]


def find_majority_elements_II_2(nums):
    t1 = t2 = n1 = n2 = 0
    for v in nums:
        if n1 != 0 and t1 == v:
            n1 += 1
        elif n2 != 0 and t2 == v:
            n2 += 1
        elif n1 == 0:
            t1 = v
            n1 += 1
        elif n2 == 0:
            t2 = v
            n2 += 1
        else:
            n1 -= 1
            n2 -= 1

    ret = []
    if n1 != 0 and nums.count(t1) > len(nums) / 3:
        ret.append(t1)
    if n2 != 0 and nums.count(t2) > len(nums) / 3:
        ret.append(t2)
    return ret

if __name__ == '__main__':
    # nums = [1, 1, 2, 3, 3, 2, 2, 4, 4, 1, 1, 1, 1]
    # nums = [i for i in range(10)]
    # nums = [5] * 8 + nums
    # nums = [6] * 8 + nums
    nums = [1,2,0,4,5,0,6,7,8,9,9,9,9,9,9,0,0,0,0,0]
    print nums, len(nums), nums.count(0)
    print find_majority_elements_II(nums)
    print find_majority_elements_II_2(nums)

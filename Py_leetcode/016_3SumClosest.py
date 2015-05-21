import sys
import math

"""
    Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
    target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
def three_sum_closest(num, target):
        n = len(num)

        num.sort()

        if n < 3:
            return 0

        if n == 3:
            return sum(num)

        i = 0
        diff = 1000000000000000
        res = 0
        while i < n - 2:
            j = i + 1
            k = n - 1

            while j < k:
                total = num[i] + num[j] + num[k]
                if abs(total - target) < diff:
                    diff = abs(total - target)
                    res = total
                
                if diff == 0:
                    return res
                elif total - target < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return res


#s = [-1, 2, 1, -4]
#print three_sum_closest(s, 1)

#s = [1, 1, 1, 0]
#print three_sum_closest(s, -100)

#s = [0, 2, 1, -3]
#print three_sum_closest(s, 1)

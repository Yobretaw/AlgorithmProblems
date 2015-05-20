import sys
import math

"""
    Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
    Find all unique quadruplets in the array which gives the sum of target.

    Note:
    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
    The solution set must not contain duplicate quadruplets.
        For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

        A solution set is:
        (-1,  0, 0, 1)
        (-2, -1, 1, 2)
        (-2,  0, 0, 2)
"""
def four_sum(num, target):
    n = len(num)
    
    if n < 4:
        return []

    num.sort()

    if n == 4:
        return [num] if sum(num) == target else []

    i = 0
    res = []
    while i < n - 3:
        j = i + 1
        while j < n - 2:
            k = j + 1
            l = n - 1
            
            while k < l:
                total = num[i] + num[j] + num[k] + num[l]
                if total == target:
                    res.append([num[i], num[j], num[k], num[l]])
                    
                    k += 1
                    l -= 1

                    while k < l and num[k] == num[k - 1]: k += 1
                    while k < l and num[l] == num[l + 1]: l -= 1
                elif total < target:
                    k += 1
                    while k < l and num[k] == num[k - 1]: k += 1
                else:
                    l -= 1
                    while k < l and num[l] == num[l + 1]: l -= 1
            j += 1
            while j < n - 2 and num[j] == num[j - 1]: j += 1
        i += 1
        while i < n - 3 and num[i] == num[i - 1]: i += 1

    return res


l = [1, 0, -1, 0, -2, 2]
print four_sum(l, 0)

l = [0, 0, 0, 0, 0]
print four_sum(l, 0)

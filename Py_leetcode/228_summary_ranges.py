import re

"""
    Given a sorted integer array without duplicates, return the summary of its ranges.

    For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
def summary_ranges(nums):
    if not nums:
        return []

    n = len(nums)

    res = []
    i = 0
    while i < len(nums):
        start = nums[i]
        end = start
        j = i + 1
        while j < n and nums[j] == end + 1:
            j += 1
            end += 1
        
        if i == j - 1:
            res.append(str(start))
        else:
            res.append(str(start) + '->' + str(end))
        i = j
    return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print summary_ranges(nums)

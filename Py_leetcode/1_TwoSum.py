import sys
import math

"""
  Given an array of integers, find two numbers such that they add up to a specific target number.

  The function twoSum should return indices of the two numbers such that they add up to the target,
  where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

  You may assume that each input would have exactly one solution.

  Input: numbers={2, 7, 11, 15}, target=9
  Output: index1=1, index2=2
"""
def two_sum(num, target):
    m = {}
    for i in range(0, len(num)):
        val = num[i]
        try:
            return (m[target - val], i + 1)
        except KeyError:
            m[val] = i + 1

    return None


"""
    Test Cases
"""
num = [1, 2]
print two_sum(num, 1)
print two_sum(num, 3)


num = [3, 2, 4]
print two_sum(num, 6)

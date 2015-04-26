import sys
import math

"""
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

    The replacement must be in-place, do not allocate extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
    1,2,3 -> 1,3,2
    3,2,1 -> 1,2,3
    1,1,5 -> 1,5,1
"""
# @param num, a list of integer
# @return nothing (void), do not return anything, modify num in-place instead.
def next_permutation(num):
    n = len(num)
    i = n - 1
    while i > 0:
        if num[i] > num[i - 1]:
            break
        i -= 1

    if i == 0:
        num[:] = num[::-1]
        return

    # find the next big digit that is larger than num[i - 1] in num[i:]
    j = i
    closest_idx = j
    while j < n:
        if num[j] <= num[closest_idx] and num[j] > num[i - 1]:
            closest_idx = j
        j += 1

    # swap the next big digit with num[i - 1]
    num[i - 1], num[closest_idx] = num[closest_idx], num[i - 1]

    # reverse the rest
    j = n - 1
    while i < j:
        num[i], num[j] = num[j], num[i]
        i += 1
        j -= 1


#s = [1, 2, 3]
#next_permutation(s)
#print s

#s = [1, 3, 2]
#next_permutation(s)
#print s

#s = [3, 2, 1]
#next_permutation(s)
#print s

#s = [1, 1, 5]
#next_permutation(s)
#print s

#s = [1, 2, 3, 4, 6, 3, 5]
#next_permutation(s)
#print s

#s = [2,3,1,3,3]
#next_permutation(s)
#print s

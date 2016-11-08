import sys
import os
import math


"""
    Given an array of digits A and a nonnegative integer k, interpase multiplies
    (X) and adds (+) with digits of A such that the resulting arithemetical exp-
    ression evaluates to k. For example, if A is <1, 2, 3, 2, 5, 3, 7, 8, 5, 9>
    and k is 995, then k can be realized by the expression:

        "123 + 2 + 5 x 3 X 7 + 85 X 9"
"""
def synthesize_expression(nums, k):
    if not nums:
        return ''

    return synthesize_expression_help(nums, 1, [str(nums[0])], k)


def synthesize_expression_help(nums, idx, curr_exp, k):
    if idx == len(nums):
        if eval(''.join(curr_exp)) == k:
            return ''.join(curr_exp)
        else:
            return None

    val = str(nums[idx])
    curr_exp.append(val)
    res = synthesize_expression_help(
            nums,
            idx + 1,
            curr_exp,
            k
    )
    curr_exp.pop()
    if res:
        return res

    curr_exp.extend(['+', val])
    res = synthesize_expression_help(
            nums,
            idx + 1,
            curr_exp,
            k
    )
    curr_exp.pop()
    curr_exp.pop()
    if res:
        return res

    curr_exp.extend(['*', val])
    res = synthesize_expression_help(
            nums,
            idx + 1,
            curr_exp,
            k
    )
    curr_exp.pop()
    curr_exp.pop()
    return res

if __name__ == '__main__':
    a = [1, 2, 3, 2, 5, 3, 7, 8, 5, 9]
    for i in range(100, 1000):
        print i, synthesize_expression(a, i)

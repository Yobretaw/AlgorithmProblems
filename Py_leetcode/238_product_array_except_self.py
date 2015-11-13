import sys


"""
    Given an array of n integers where n > 1, nums, return an array output such
    that output[i] is equal to the product of all the elements of nums except
    nums[i].

    Solve it without division and in O(n).

    For example, given [1,2,3,4], return [24,12,8,6].
"""
def product_array(a):
    n = len(a)

    if n < 2:
        return a

    res = list(a)

    a[0] = 1
    for i in range(1, n):
        a[i] = a[i - 1] * res[i - 1]

    tmp = res[-1]
    res[-1] = 1
    for i in reversed(range(0, n - 1)):
        t = res[i]
        res[i] = tmp * res[i + 1]
        tmp = t

    for i in range(1, n):
        res[i] *= a[i]

    return res

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    a = [9, 0, -2]
    print product_array(a)

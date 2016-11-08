import sys
import math

"""
    Let array A be an array of n positive integers. Design an algorithm that
    computes a subset S of A such that |sum(S) - sum(A - S)| is minimized.
"""
def split_array(arr):
    n = len(arr)
    total = sum(arr)

    # t[i][j] indices whether we can achieve a sum of j using the first i
    # elements of array
    t = [[False for i in range(total + 1)] for i in range(n + 1)]
    t[0][0] = True

    for i in range(1, n + 1):
        for j in range(total + 1):
            t[i][j] |= t[i - 1][j]

            if j >= arr[i - 1]:
                t[i][j] |= t[i - 1][j - arr[i - 1]]

    # return the number of combination of subsets that yield a tie
    val = total / 2 
    while val >= 0 and not t[-1][val]:
        val -= 1
    return total - 2 * val

"""
    Variant 17.10.1

    Solve the same problem with the additional cnostraint that the subsets must
    have equal size.
"""
def split_array2(arr):
    if len(arr) & 1:
        return None

    min_val = [sys.maxint]
    res = []
    split_array_help2(arr, 0, 0, min_val, [], res)
    return min_val[0], res

def split_array_help2(arr, idx, diff, min_val, curr, res):
    if idx == len(arr):
        if len(curr) == len(arr) / 2:
            if min_val[0] > abs(diff):
                res[:] = list(curr)
            min_val[0] = min(min_val[0], abs(diff))
        return
    
    if len(curr) < len(arr) / 2:
        curr.append(arr[idx])
        split_array_help2(arr, idx + 1, diff + arr[idx], min_val, curr, res)
        curr.pop()

    split_array_help2(arr, idx + 1, diff - arr[idx], min_val, curr, res)



if __name__ == '__main__':
    arr = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
    print split_array(arr)
    print split_array2(arr)

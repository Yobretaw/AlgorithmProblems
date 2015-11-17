import sys
from heapq import *
from collections import deque

"""
    Given an array nums, there is a sliding window of size k which is moving
    from the very left of the array to the very right. You can only see the k
    numbers in the window. Each time the sliding window moves right by one
    position.

    For example,
    Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    Therefore, return the max sliding window as [3,3,5,5,6,7].

    Note: 

    You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty
    array.
"""
def sliding_window_maximum(nums, k):
    res = []

    # q stores the indices of elements in current window
    # we ensure that q[-1] <= q[-2]
    q = deque()
    for i, v in enumerate(nums):
        if q and q[0] <= i - k:
            q.popleft()

        # ensure q[-1] <= q[-2]
        while q and nums[q[-1]] < v:
            q.pop()

        q.append(i)
        if i + 1 >= k:
            res.append(nums[q[0]])

    return res


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print sliding_window_maximum(nums, k)

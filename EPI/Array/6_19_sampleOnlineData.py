import sys
import os
import re
import math
import random


"""
    ============================================================================================
    Design an algorithm that reads packets and continuously maintains a uniform random subset of
    size k of the packet after n >= k-th packets are read.
    ============================================================================================

    Solution: The idea is to process each new packet incrementally. We store the first k packets.
    After these k packets, the n > k-th packets belongs to the random subset with probability k/n.
    If we choose the n-th packet, we select an existing element uniformlly at random to eject from
    subset.


    line = sys.stdin.readline()
    while line:
        ...
        line = sys.stdin.readline()

"""
def randomOnlineData(k):
    sampling_result =[]
    line = sys.stdin.readline()

    # the first k elements
    for i in range(0, k):
        if not line:
            break

        sampling_result.append(line)
        line = sys.stdin.readline()

    # after the first k elements
    element_count = k
    while line:
        pos = random.randint(0, element_count)
        if pos < k:
            sampling_result[pos] = line

        element_count += 1
        line = sys.stdin.readline()

    return sampling_result


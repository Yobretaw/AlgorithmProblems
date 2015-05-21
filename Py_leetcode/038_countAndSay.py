import sys
import math

"""
    The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n, generate the nth sequence.

    Note: The sequence of integers will be represented as a string.
"""
def count_and_say(n):
    if n == 1:
        return '1'

    res = [1]
    for i in range(1, n):
        curr = []
        i = 0
        while i < len(res):
            j = i + 1
            while j < len(res):
                if res[j] != res[i]:
                    break
                j += 1
            curr.append(j - i)
            curr.append(res[i])
            i = j
        res = curr

    return ''.join([str(x) for x in res])


#for i in range(1, 30):
#    print count_and_say(i)

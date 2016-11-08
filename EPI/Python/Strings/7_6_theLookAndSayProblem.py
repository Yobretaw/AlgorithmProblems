import sys
import os
import re
import math

"""
    ============================================================================================
    In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

        1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... (sequence A005150 in OEIS).

    To generate a member of the sequence from the previous member, read off the digits of the previous member,
    counting the number of digits in groups of the same digit. For example:

    - 1 is read off as "one 1" or 11.
    - 11 is read off as "two 1s" or 21.
    - 21 is read off as "one 2, then one 1" or 1211.
    - 1211 is read off as "one 1, then one 2, then two 1s" or 111221.
    - 111221 is read off as "three 1s, then two 2s, then one 1" or 312211.
    
    Write a function that takes as input an integer n and returns the n-th integer in the look-and-say
    sequence.
    ============================================================================================
"""
def look_and_say(n):
    if n == 0:
        return None

    if n == 1:
        return 1

    res = "11"
    for i in range(1, n):
        tmp = ""
        res_len = len(res)

        start = 1
        count = 1
        while start < res_len:
            if res[start] != res[start - 1]:
                tmp += str(count) + res[start - 1]
                count = 1
            else:
                count += 1

            start += 1

        tmp += str(count) + res[start - 1]
        res = tmp

    return int(res)

print look_and_say(10)


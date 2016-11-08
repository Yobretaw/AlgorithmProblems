import sys
import os
import re
import math

"""
    ============================================================================================
    Run-lenght encoding (RLE) compression offers a fast way to do efficient on-the-fly compression
    and decompression of strings. The idea is simple - encode successive repeated characters by
    the repetition count and the character. For exmaple, the RLE of "aaaabcccaa" is "4a1b3c2a".
    The decoding of "3e4f2e" returns "eeeffffeee".

    Implement run-lenght encode and decoding functions. Assume the strings to be encoded consists
    of letters of alphabet, with no digits, and the string to be decoded is a valid encoding.
    ============================================================================================
"""
def encode(s):
    n = len(s)

    if n < 2:
        return s

    res = ""
    idx = 1
    count = 1
    while idx < n:
        if s[idx] != s[idx - 1]:
            res += str(count) + s[idx - 1]
            count = 1
        else:
            count += 1

        idx += 1

    res += str(count) + s[idx - 1]
    return res



def decode(s):
    n = len(s)

    if n == 0:
        return ""

    res = ""
    for i in range(0, n / 2):
        count = int(s[2 * i])
        char = s[2 * i + 1]

        res += char * count
    
    return res


print encode("aaaabcccaa")
print encode("eeeffffeee")
print decode(encode("aaaabcccaa"))
print decode(encode("eeeffffeee"))

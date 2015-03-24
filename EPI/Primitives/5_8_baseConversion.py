import sys
import os
import re
import math


def convert(s, b1, b2):
    val = 0
    m = 1

    for c in reversed(s):
        val += (ord(c) - ord('0') if c <= '9' else 10 + (ord(c) - ord('A'))) * m
        m *= b1

    result = ""
    while True:
        remainder = val % b2
        result += chr(ord('A') + remainder - 10) if remainder >= 10 else str(remainder)
        val /= b2

        if not val:
            break

    return result[::-1]


print(convert("615", 7, 13))



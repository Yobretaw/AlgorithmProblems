import sys
import os
import re
import math

"""
    ============================================================================================
    We illustrate what it means to write a string in sinusoidal fashion by mean of an exmaple.
    The string "Hello_World!" written in sinusoidal fashion is 

      e       _       l
    h   l   o   W   r   d
          l       o       !

    Define the snakestring of s to be the left-right top-to-bottom sequence in which characters
    appears when s is written in sinusodial fashion. For example, the snakestring for "Hello_World"
    is "e_lhloWrdlo!"
    ============================================================================================
"""
def snakestring(s):
    n = len(s)

    idx = 1
    res = ""
    while idx < n:
        res += s[idx]
        idx += 4

    idx = 0
    while idx < n:
        res += s[idx]
        idx += 2

    idx = 3
    while idx < n:
        res += s[idx]
        idx += 4

    return res


print snakestring("Hello_World!")

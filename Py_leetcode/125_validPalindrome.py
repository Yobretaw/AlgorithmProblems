import sys
import os
import math
import imp

"""
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    For example,
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

    Note:
    Have you consider that the string might be empty? This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.
"""
def is_palindrome(s):
    n = len(s)
    if n < 2:
        return True

    s = s.lower().strip()
    start, end = 0, n - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        else:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
    return True


def is_palindrome2(s):
    s = filter(str.isalnum, str(s)).lower()
    return s == s[::-1]

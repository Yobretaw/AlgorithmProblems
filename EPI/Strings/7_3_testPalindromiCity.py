import sys
import os
import re
import math

"""
    ============================================================================================
    Implement a function which takes as input a string s and returns true if s is a palindrome
    string. Note nonalphanumeric can be ignored.
    ============================================================================================
"""
def isPalindrome(s):
    n = len(s)

    if n < 2:
        return True

    start = 0
    end = n - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1

        while start < end and not s[end].isalnum():
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True

print isPalindrome("A man, a plan, a canal, Panama.")
print isPalindrome("Able was I, ere I saw Elba!")
print isPalindrome("Ray a Ray")


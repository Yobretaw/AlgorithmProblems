import sys
import math

"""
    Given a string, find the length of the longest substring without repeating characters.

    For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
    For "bbbbb" the longest substring is "b", with the length of 1.
"""
def length_of_longest_substring(s):
        curr_start = 0
        max_len = 0
        chars = [-1] * 256
        for i in range(0, len(s)):
            k = ord(s[i])
            if chars[k] >= curr_start:
                curr_start = chars[k] + 1

            chars[k] = i

            max_len = max(i - curr_start + 1, max_len)

        return max_len

"""
    Test Cases
"""

s = "abcabcbb"
print length_of_longest_substring(s)

s = "bbbbbb"
print length_of_longest_substring(s)

s = "c"
print length_of_longest_substring(s)

s = "aab"
print length_of_longest_substring(s)

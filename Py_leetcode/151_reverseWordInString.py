import sys
import os
import math

"""
    Given an input string, reverse the string word by word.

    For example,
    Given s = "the sky is blue",
    return "blue is sky the".

    Clarification:
    What constitutes a word?

        - A sequence of non-space characters constitutes a word.

    Could the input string contain leading or trailing spaces?
        - Yes. However, your reversed string should not contain leading or trailing spaces.

    How about multiple spaces between two words?

        - Reduce them to a single space in the reversed string.
"""
def reverseWord(s):
    if not s:
        return s

    s = [c for c in s.strip().split(' ') if c != '']
    return ' '.join([c for c in s][::-1])


def reverseWord2(s):
    """
        s is an array of characters
    """
    if not s:
        return s

    idx = 0
    n = len(s)
    while idx < n:
        i = idx
        while i < n and s[i].isspace():
            i += 1

        j = i
        while j < n and not s[j].isspace():
            j += 1

        idx = j
        j -= 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    s[:] = s[::-1]
    return ''.join(s)


#print reverseWord('a  b')
#print reverseWord2([c for c in 'A sequence of non-space characters constitutes a word.'])

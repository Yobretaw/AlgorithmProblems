import sys
import os
import re
import math

"""
    ============================================================================================
    Write a function which takes as input a string s, and removes each "b" and replaces each 'a' by
    "dd", Assume s is stored in an array that has enough space for the final result
    ============================================================================================
"""
def modify(s):
    n = len(s)

    if n == 0:
        return

    for i in range(0, n):
        c = s[i]

        if c == 'a':
            s[i] = "dd"
        elif c == 'b':
            s[i] = ''
        else:
            pass

    s[:] = [c for c in ''.join(s)]
    return

def modify2(s):
    """
        In-place modify, assume s is stored in an array that has enough space for the final result
    """
    n = len(s)

    if n == 0:
        return

    # first we remove 'b's
    curr = 0
    last = 0
    count_a = 0
    for i in range(0, n):
        if s[curr] == 0:
            break
        elif s[curr] == 'b':
            curr += 1
        else:
            if s[curr] == 'a':
                count_a += 1

            s[last] = s[curr]
            last += 1
            curr += 1

    s[:] = s[:last + count_a]

    curr = last - 1
    last = len(s) - 1
    while curr >= 0:
        if s[curr] == 'a':
            s[last] = s[last - 1] = 'd'
            last -= 2
            curr -= 1
        else:
            s[last] = s[curr]
            curr -= 1
            last -= 1
    return


##s = 'abcd'
##s = 'aabbccddabcd'
#s = 'aaaaaa'
#s = [c for c in s]
#s.extend([0] * len(s))
#modify2(s)
#print ''.join(s)
#print len(s)


"""
    Variant 7.2.1: You have an array C of characters. the characters may be letters, digits, blanks, and punctuation. 
    The text-encoding of the array C is an array T of characters in which letters, digits, and blanks appear as before,
    but punctuation marks are spelled out. For example, telex-encoding entails replacing the character "." by "DOT",
    the character "," by "COMMA", the character "?" by "QUESTION MARK", and the character "!" by "EXCLAMATION MARK".
    Design an algorithm to perform telex-encoding with O(1) space.
"""
def telex_encoding(s):
    n = len(s)

    if n == 0:
        return

    extra_len = 0
    i = 0
    while i < n:
        if s[i] == '\0':
            break

        sym = parse_punchunation(s[i])
        if sym:
            extra_len += len(sym[1]) - len(sym[0])
        else:
            pass

        i += 1

    s[:] = s[:i + extra_len]
    curr = i - 1
    last = len(s) - 1

    while curr >= 0:
        sym = parse_punchunation(s[curr])
        print sym
        if not sym:
            s[last] = s[curr]
            last -= 1
            curr -= 1
        else:
            for i in reversed(range(0, len(sym[1]))):
                s[last] = sym[1][i]
                last -= 1
            curr -= 1
    return

def parse_punchunation(c):
    DOT = (".", "DOT")
    COMMA = (",", "COMMA")
    QUESTION_MARK = ("?", "QUESTION_MARK")
    EXCLAMATION_MARK = ("!", "EXCLAMATION_MARK")

    if c == DOT[0]:
        return DOT
    elif c == COMMA[0]:
        return COMMA
    elif c == QUESTION_MARK[0]:
        return QUESTION_MARK 
    elif c == EXCLAMATION_MARK[0]:
        return EXCLAMATION_MARK
    else:
        return None

#s = "hello. world!"
#s = "!.,?"
#s = [c for c in s]
#s.extend(['\0'] * 50)
#telex_encoding(s)
#print ''.join(s)


"""
    Variant 7.2.2: Write a function which meges two sorted arrays of integers, A and B. Specifically, the final result
    would be a sorted array of length m + n, where n and  are the lengths of A and B,respectively. Use O(1) additional
    space - assume the result is stored in A, which has sufficient space. These arrays are C-style arrays, i.e., conti-
    guous preallocated blocks of memory
"""
def merge_sorted_arrays(A, B):
    pass


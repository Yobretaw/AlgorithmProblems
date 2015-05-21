import sys
import os
import math

"""
    Given an array of words and a length L, format the text such that each line has exactly L characters
    and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
    Pad extra spaces ' ' when necessary so that each line has exactly L characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a
    line do not divide evenly between words, the empty slots on the left will be assigned more spaces than
    the slots on the right.

    For the last line of text, it should be left justified and no extra space is inserted between words.

    For example,
    words: ["This", "is", "an", "example", "of", "text", "justification."]
    L: 16.

    Return the formatted lines as:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]

    Note: Each word is guaranteed not to exceed L in length.

    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
"""
def text_justification(words, width):
    if not words or not width:
        return words

    n = len(words)
    res = []
    idx = 0
    while idx < n:
        curr_line_words = []
        curr_line_ws = []
        curr_line_len = 0
        while idx < n and curr_line_len < width:
            w = words[idx]
            if curr_line_len + (1 if curr_line_words else 0) + len(w) <= width:
                if curr_line_words:
                    curr_line_ws.append(' ')
                    curr_line_len += 1
                curr_line_words.append(w)
                curr_line_len += len(w)
                idx += 1
            else:
                break

        extra_len = width - curr_line_len
        if extra_len:
            if not curr_line_ws or idx == n:
                curr_line_ws.append(' ')
                extra_len -= 1
            if idx == n:
                curr_line_ws[-1] += ' ' * extra_len
            else:
                i = 0
                while extra_len > 0:
                    i %= len(curr_line_ws)
                    curr_line_ws[i] += ' '
                    extra_len -= 1
                    i += 1

        line = []
        for i in range(0, len(curr_line_words)):
            line.append(curr_line_words[i] + (curr_line_ws[i] if i < len(curr_line_ws) else ''))
        res.append(''.join(line))
    return res

#print text_justification([""], 0)
#print text_justification(["What","must","be","shall","be."], 12)
#print text_justification(["a"], 1)
#print text_justification(["Listen","to","many,","speak","to","a","few."], 6)
#print text_justification(["This", "is", "an", "example", "of", "text", "justification."], 16)

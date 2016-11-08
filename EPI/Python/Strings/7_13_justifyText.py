import sys
import os
import re
import math

"""
    ============================================================================================
    Given an array of words and a length L, format the text such that each line has exactly L characters and
    is fully (left and right) justified.
    
    You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
    Pad extra spaces ' ' when necessary so that each line has exactly L characters.
    
    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line
    do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
    
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
    
    Corner Cases:
    A line other than the last line might contain only one word. What should you do in this case?
    In this case, that line should be left-justified.
        
    ============================================================================================
"""
def justify_text(words, L):
        n = len(words)

        if n == 0:
            return ""

        if n == 1:
            return [words[0].ljust(L)]

        lines = []
        idx = 0
        while idx < n:
            curr_line = []
            l = 0
            while idx < n and (l + len(words[idx])) <= L:
                curr_line.append(words[idx])
                curr_line.append(' ')

                l += len(words[idx]) + 1
                idx += 1
            
            # remove the last space in curr_line
            curr_line.pop()
            lines.append(curr_line)

        for i in range(0, len(lines) - 1):
            line = lines[i]
            line_len = sum(len(s) for s in line)

            extra_space = L - line_len
            num_space = len(line) / 2
            avg_space_len = (extra_space / num_space) if num_space > 0 else 0
            remain_space = extra_space - num_space * avg_space_len

            extra_space -= remain_space
            for j in range(0, len(line)):
                if not line[j].isspace():
                    continue

                if remain_space > 0:
                    line[j] += ' '
                    remain_space -= 1
                if extra_space > 0:
                    line[j] += ' ' * avg_space_len

            if remain_space > 0:
                lines[i].append(' ' * remain_space)

        # add extra spaces for the last line
        last_len = sum(len(s) for s in lines[-1])
        if L - last_len > 0:
            lines[-1].append(' ' * (L - last_len))

        lines = [''.join(line) for line in lines]
        return lines
            

#print justify_text([""], 0)
#print justify_text(["This", "is", "an", "example", "of", "text", "justification."], 16)
#print justify_text(["a","b","c","d","e"], 3)
#print justify_text(["Listen","to","many,","speak","to","a","few."], 6)
#print justify_text(["What","must","be","shall","be."], 12)


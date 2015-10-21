import os
import math
import sys
import random
from collections import defaultdict, Counter

"""
    Writa a function which takes as input a string(the 'sentence') and a list
    of strings(the 'words'), and returns all substrings of the sentence string
    which are the concatenation of all the words. Each word must appear exactly
    once, and the ordering is immaterial. Assume all words have equal length.
"""
# assuming no duplicates in words
def find_all_substring(s, words):
    if not s or not words:
        return []

    n = len(s)
    word_count = len(words)
    word_len = len(random.sample(words, 1)[0])

    res = []
    for i in range(n - word_count * word_len + 1):
        end = i + word_count * word_len

        curr_words = set()
        for j in range(i, end, word_len):
            curr_word = s[j:j+word_len]
            if not curr_word in words:
                break

            curr_words.add(curr_word)

        if len(curr_word) == len(curr_words) and curr_words == words:
            res.append(s[i:end])

    return res

# assuming duplicates are allowed in words
def find_all_substring_with_duplicates(s, words):
    if not s or not words:
        return []

    word_set = defaultdict(int)
    for w in words:
        word_set[w] += 1

    n = len(s)
    res = []
    word_count = len(words)
    word_len = len(words[0])

    for i in range(n - word_count * word_len + 1):
        end = i + word_count * word_len
        count = len(words)

        curr_words = defaultdict(int)
        for j in range(i, end, word_len):
            curr_word = s[j:j+word_len]
            if not curr_word in word_set:
                break

            curr_words[curr_word] += 1
            if curr_words[curr_word] > word_set[curr_word]:
                break
        else:
            res.append(s[i:end])
    return res

if __name__ == '__main__':
    print find_all_substring('amanaplanacanal', set(['can', 'apl', 'ana']))
    print find_all_substring('amanaplanacanal', set(['ap', 'la']))

    print find_all_substring_with_duplicates('amanaplanacanal', ['can', 'apl', 'ana'])
    print find_all_substring_with_duplicates('amanaplanacanal', ['ap', 'la'])

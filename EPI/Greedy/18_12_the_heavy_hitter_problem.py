import sys
import math

"""
    You are reading a sequence of strings separated by whitespaces. You are
    allowed to read the sequence twice. Devise an algorithm that uses O(k)
    memory to identify the words that occur at least ceil(n/k) times, where
    n is the length of the sequence.

    ----

    Idea:

    We discard k words at any given time and we are guaranteed that all the
    words that occured more than 1/k times the length of the sequence prior
    to the discarding continue to appear more than 1/k times in the remaining
    sequence.
"""
def find_heavy_hitter(words, k):
    n = len(words)
    if n < k:
        return words

    # a dictionary that maps word to their number of occurences
    d = {}

    # first pass yields a set S of no more than k words; set S is a super set
    # of the words that occur greater than or equal to n / k times.
    for w in words:
        if w in d:
            d[w] += 1
        elif len(d) < 5:
            d[w] = 1
        else:
            key_to_remove = []
            for key in d.keys():
                d[key] -= 1
                if not d[key]:
                    key_to_remove.append(key)

            for key in key_to_remove:
                d.pop(key)

    # second pass: filter out those that appear less than to n/k times
    for key in d.keys():
        d[key] = 0

    for w in words:
        if w in d:
            d[w] += 1

    return [key for key in d if d[key] >= math.ceil(n/k)]


if __name__ == '__main__':
    A = [1, 1, 2, 3, 1, 2, 2, 2, 2, 2]
    k = 2
    print find_heavy_hitter(A, k)

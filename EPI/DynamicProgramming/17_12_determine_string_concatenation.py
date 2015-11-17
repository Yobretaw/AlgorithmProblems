import sys
import math

"""
    Given a dictionary, i.e., a set of strings, and a string s, design an
    algorithm that checks whether s is the concatenation of a sequence of
    dictionary words. If such a concatenation exists, output it.
"""
def find_concatanation_word(d, s):
    if not s or not d:
        return None

    res = []
    if find_concatanation_word_help(d, s, 0, [], res, set()):
        return res[0]
    return []


def find_concatanation_word_help(d, s, idx, curr, res, seen):
    if idx == len(s):
        res.append(list(curr))
        return True

    if idx in seen:
        return False

    for i in range(idx + 1, len(s) + 1):
        ss = s[idx:i]
        if ss in d:
            curr.append(ss)
            if find_concatanation_word_help(d, s, i, curr, res, seen):
                return True
            curr.pop()

    seen.add(idx)
    return False


# Time: O(n^2*W) where n = len(s) and W = length of longest word in dictionary
# (note each string slice cost (i - j) time)
def find_concatanation_word2(d, s):
    n = len(s)

    # t[i] stores the length of the last word in the string that ends at i
    t = [0] * n

    max_word_len = max(len(ss) for ss in d)

    for i in range(n):
        if s[:i + 1] in d:
            t[i] = i + 1
            continue

        for j in range(i - max_word_len, i):
            if t[j] and s[j + 1:i + 1] in d:
                t[i] = i - j
                break

    if not t[-1]:
        return []

    ret = []
    idx = n - 1
    while idx >= 0:
        ret.append(s[idx - t[idx] + 1:idx + 1])
        idx -= t[idx]
    return ret[::-1]


"""
    Variant 17.12.1

    Devise an O(nW) algorithm for word breaking
"""
# TODO


if __name__ == '__main__':
    d = set("Given a dictionary, i.e., a set of strings, and a string s, design an algorithm that checks whether s is the concatenation of a sequence of dictionary words. If such a concatenation exists, output it.".replace('.', '').replace(',', '').split(' '))
    print find_concatanation_word(d, 'setdesignGivenofdictionarywordssuchoutputconcatenation')
    print find_concatanation_word2(d, 'setdesignGivenofdictionarywordssuchoutputconcatenation')

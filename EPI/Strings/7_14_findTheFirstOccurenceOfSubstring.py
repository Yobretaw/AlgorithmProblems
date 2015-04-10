import sys
import os
import re
import math

"""
    ============================================================================================
    Given two strings s(the "search string") and t(the "text"), find the first occurence of s in
    t.

    If someone asks you this question in an interview, the best way to approach this problem would
    be to work through one good algorithm in detail and discuss at a high level of other algorithms
    ============================================================================================
"""
def karp_rabin_string_search(s, t):
    m = len(s)
    n = len(t)

    dm = 1
    h1 = 0
    h2 = 0

    q = 3355439
    d = 256

    for i in range(1, m):
        dm = (d * dm) % q

    for i in range(0, m):
        h1 = (h1 * d + ord(s[i])) % q
        h2 = (h2 * d + ord(t[i])) % q

    if h1 == h2 and s == t[0:m]:
        return 0

    for i in range(m, n):
        h2 = (h2 - ord(t[i - m]) * dm) % q
        h2 = (h2 * d + ord(t[i])) % q

        print h1, h2
        if h1 == h2 and s == t[i-m+1:i+1]:
            return i - m + 1

    return -1

print karp_rabin_string_search("wor", "hello world")
print karp_rabin_string_search("cannot", "The Naive String Matching algorithm slides the pattern one by one. After each slide, it one by one checks characters at the current shift and if all characters match then prints the match.Like the Naive Algorithm, Rabin-Karp algorithm also slides the pattern one by one. But unlike the Naive algorithm, Rabin Karp algorithm matches the hash value of the pattern with the hash value of current substring of text, and if the hash values match then only it starts matching individual characters. So Rabin Karp algorithm needs to calculate hash values for following strings.1) Pattern itself.2) All the substrings of text of length m.Since we need to efficiently calculate hash values for all the substrings of size m of text, we must have a hash function which has following property.Hash at the next shift must be efficiently computable from the current hash value and next character in text or we can say hash(txt[s+1..s+m]) must be efficiently computable from hash(txt[s .. s+m-1]) and txt[s+m] i.e., hash(txt[s+1 .. s+m])= rehash(txt[s+m], hash(txt[s .. s+m-1]) and rehash must be O(1) operation.The hash function suggested by Rabin and Karp calculates an integer value. The integer value for a string is numeric value of a string. For example, if all possible characters are from 1 to 10, the numeric value of '122' will be 122. The number of possible characters is higher than 10 (256 in general) and pattern length can be large. So the numeric values cannot be practically stored as an integer. Therefore, the numeric value is calculated using modular arithmetic to make sure that the hash values can be stored in an integer variable (can fit in memory words). To do rehashing, we need to take off the most significant digit and add the new least significant digit for in hash value. Rehashing is done using the following formula.")
#print karp_rabin_string_search("wor", "aword")

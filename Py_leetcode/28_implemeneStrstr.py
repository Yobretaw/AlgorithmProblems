import sys
import math

"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
def strstr(haystack, needle):
        m = len(haystack)
        n = len(needle)

        if not m or m < n:
            return -1

        for i in range(0, m - n + 1):
            j = 0
            while j < n and haystack[i + j] == needle[j]: j += 1

            if j == n:
                return i

        return -1

#print strstr("Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack", "haystack")

import sys
import math

"""
    Implement atoi to convert a string to an integer.

    -   Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
    You are responsible to gather all the input requirements up front.

    -   The function first discards as many whitespace characters as necessary until the first non-whitespace character
    is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many
    numerical digits as possible, and interprets them as a numerical value.

    -   The string can contain additional characters after those that form the integral number, which are ignored
    and have no effect on the behavior of this function.

    -   If the first sequence of non-whitespace characters in str is not a valid integral number, or if
    no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    -   If no valid conversion could be performed, a zero value is returned. If the correct value is
    out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""
def strToInt(s):
    n = len(s)

    if n < 2:
        try:
            return int(s)
        except ValueError:
            return 0

    s = s.strip()
    i = 0
    res = 0
    sign = 1
    if s[i] == '-' or s[i] == '+':
        sign = 1 if s[i] == '+' else -1
        i += 1

    while i < len(s) and s[i].isdigit():
        if sign > 0 and res > (sys.maxint - int(s[i])) / 10:
            return sys.maxint
        elif sign < 0 and res + 1 > (sys.maxint - int(s[i])) / 10:
            return - sys.maxint - 1

        res *= 10
        res += int(s[i])
        i += 1

    return 0 if i < len(s) else sign * res


#print sys.maxint
#print strToInt('9223372036854775807')
#print strToInt('9223372036854775808')
#print strToInt('-9223372036854775808')
#print strToInt('-9223372036854775809')

import sys
import os
import re
import math

"""
    ============================================================================================
    Write a function that determines where to add periods to the decimal string so that the
    resulting string is a valid IP address. There may be more than one valid IP address corresponding
    to a string, in which case you should return all possiblilities.
    ============================================================================================
"""
def compute_possible_ip(s):
    n = len(s)

    if n < 4 or n > 12:
        return []

    res = []
    generate_ips(0, 3, "", s, res)

    res_arr = [s.split('.') for s in res]
    res = ['.'.join(s) for s in res_arr if is_valid_parts(s)]
    return res


def generate_ips(idx, left, curr, s, result):
    n = len(s)

    if left == 0:
        if n - idx > 3:
            return
        else:
            curr += s[idx:]
            result.append(curr)
            return

    for i in range(idx + 1, min(idx + 4, n)):
        tmp = curr + s[idx:i] + '.'
        generate_ips(i, left - 1, tmp, s, result)

def is_valid_parts(s):
    for val in s:
        n = len(val)
        if n == 2 and val[0] == '0':
            return False
        elif n == 3 and int(val) > 255:
            return False

    return True

def compute_possible_ip_without_recursion(s):
    n = len(s)

    if n < 4 or n > 12:
        return False

    result = []
    for i in range(1, min(4, n - 2)):
        first = s[0:i]
        if not is_valid_parts([first]):
            continue
        for j in range(i + 1, min(i + 4, n - 1)):
            second = s[i:j]
            if not is_valid_parts([second]):
                continue
            for k in range(j + 1, min(j + 4, n)):
                if n - k > 3:
                    continue

                third = s[j:k]
                last = s[k:]
                if not is_valid_parts([third]) or not is_valid_parts([last]):
                    continue

                result.append(first + "." + second + "." + third + "." + last)

    return result

    

print compute_possible_ip("0000")
print compute_possible_ip("999999")
print compute_possible_ip("19216811")
print compute_possible_ip("255255255255")
print '-'*100
print compute_possible_ip_without_recursion("0000")
print compute_possible_ip_without_recursion("999999")
print compute_possible_ip_without_recursion("19216811")
print compute_possible_ip_without_recursion("255255255255")

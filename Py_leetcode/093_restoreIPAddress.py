import sys
import os
import math

"""
    Given a string containing only digits, restore it by returning all possible valid IP address combinations.

    For example:
    Given "25525511135",

    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
def restore_ips(s):
    if len(s) < 4:
        return []

    res = generate_ips(s)
    res = ['.'.join(s) for s in res if is_valid_ip(s)]
    return res

def generate_ips(s):
    res = []
    generate_ips_help(s, [], res)
    return res

def generate_ips_help(s, curr, res):
    if not s:
        if len(curr) == 4:
            res.append(list(curr))
        return
    
    if len(curr) >= 4:
        return

    for i in range(1, min(3, len(s)) + 1):
        curr.append(s[:i])
        generate_ips_help(s[i:], curr, res)
        curr.pop()

def is_valid_ip(s):
    for val in s:
        if not val or val[0] == '0' and len(val) > 1 or int(val) > 255:
            return False
    return True


def restore_ips_iterative(s):
    n = len(s)
    if n < 4:
        return []

    res = []
    curr = []
    for i in range(1, min(n, 3) + 1):
        if not is_valid_ip([s[:i]]):
            continue

        curr.append(s[:i])
        for j in range(i + 1, min(n, i + 3) + 1):
            if not is_valid_ip([s[i:j]]):
                continue

            curr.append(s[i:j])
            for a in range(j + 1, min(n, j + 3) + 1):
                if n - a > 3 or not is_valid_ip([s[j:a]]) or not is_valid_ip([s[a:]]):
                    continue

                curr.extend([s[j:a], s[a:]])
                res.append('.'.join(curr))
                curr[-2:] = []
            curr.pop()
        curr.pop()
    return res


#s = '25525511135'
#s = '0000'
#s = '1111'
#s = '123123123'
#for s in restore_ips_iterative(s):
#    print s

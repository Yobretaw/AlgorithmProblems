import sys
import math

"""
    Given a digit string, return all possible letter combination that the number
    could represent.
    
    The mapping of digit to letter:
       2: a, b, c
       3: d, e, f
       4: g, h, i
       5: j, k, l
       6: m, n, o
       7: p, q, r
       8: s, t, u
       9: v, w, x, z
    
       Input:Digit string "23"
       Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""
def lettersToPhoneNumber(s):
        m = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ''
        }

        n = len(s)
        if n == 1:
            return []

        res = {}
        for c in m[s[0]]:
            res[c] = 1

        for i in range(1, n):
            curr = s[i]
            removed = res.keys()
            for key in removed:
                for c in m[curr]:
                    res[key + c] = 1
            for key in removed:
                res.pop(key, None)

        return res.keys()

#print lettersToPhoneNumber('233')


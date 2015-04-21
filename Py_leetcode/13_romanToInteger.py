import sys
import math

"""
    Given a roman numeral, convert it to an integer.

    Input is guaranteed to be within the range from 1 to 3999.
"""
def romanToInteger(x):
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    res = m[x[0]]
    for i in range(1, len(x)):
        if m[x[i]] > m[x[i - 1]]:
            res -= 2 * m[x[i - 1]]
            res += m[x[i]]
        else:
            res += m[x[i]]

    return res


#print romanToInteger('MV')

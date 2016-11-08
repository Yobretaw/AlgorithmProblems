import sys
import os
import re
import math

"""
    ============================================================================================
    Consider the phone keypad shown below:

                    1       2       3
                           ABC     DEF

                    4       5       6
                   GHI     JKL     MNO

                    7       8       9
                   PQRS    TUV     WXYZ

                    *       0       #

    Write a function which takes as input a phone number, specified as a string of digits, and
    return all possible character sequences that corresponding to the phone number. The character
    sequences do not have to be legal words or phrases.
    ============================================================================================
"""
def possible_sequences(s):
    n = len(s)

    if n == 0:
        return None

    m = {
        '1': "",
        '2': "ABC",
        '3': "DEF",
        '4': "GHI",
        '5': "JKL",
        '6': "MNO",
        '7': "PQRS",
        '8': "TUV",
        '9': "WXYZ",
        '0': ""
    }

    for num in m:
        m[num] = [c for c in m[num]]

    idx = 0
    while len(m[s[idx]]) == 0:
        idx += 1

    result = {}
    for c in m[s[idx]]:
        result[c] = 1
    
    idx += 1
    for i in range(idx, n):
        num = s[i]
        for ss in result.keys():
            for c in m[num]:
                result[ss + c] = 1
            result.pop(ss)

    return result.keys()



print possible_sequences("2276696")

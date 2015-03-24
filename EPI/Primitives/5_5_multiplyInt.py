import sys
import os
import re
import math

def multiply(x, y):
    result = 0
    while x:
        if x & 1:
            result = addHelp(result, y)

        x >>= 1
        y <<= 1

    return result

def addHelp(a, b):
    result = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b

    while temp_a or temp_b:
        ak = a & k
        bk = b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        result |= (ak ^ bk ^ carryin)

        carryin = carryout << 1
        k <<= 1
        temp_a >>= 1
        temp_b >>= 1

    return result | carryin

print multiply(0, 0)
print multiply(3, 0)
print multiply(0, 3)
print multiply(1, 1)
print multiply(2, 2)
print multiply(11, 5)
print multiply(5, 11)
print multiply(11, 11)
        


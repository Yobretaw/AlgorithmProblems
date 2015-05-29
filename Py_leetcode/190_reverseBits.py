import sys
import os
import re
import math

"""
    Reverse bits of a given 32 bits unsigned integer.

    For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
    return 964176192 (represented in binary as 00111001011110000010100101000000).

    Follow up:
    If this function is called many times, how would you optimize it?
"""
def reverse_bits(n):
    if not n:
        return n

    res = 0
    for i in range(0, 32):
        if n & (1 << (31 - i)):
            res |= 1 << i

    return res


class FastReverse:
    def __init__(self):
        self.m = None
        self.calc_reverse_map()
        
    def calc_reverse_map(self):
        self.m = [0] * (2 ** 8)
        for i in range(2 ** 8):
            self.m[i] = self.reverse_bits(i) >> 24

    def reverse_bits(self, n):
        res = 0
        for i in range(0, 32):
            if n & (1 << (31 - i)):
                res |= 1 << i

        return res

    def reverseBits(self, n):
        m = self.m
        return m[(n & 0xFF)] << 24 \
             | m[(n >> 8) & 0xFF] << 16 \
             | m[((n >> 16) & 0XFF)] << 8 \
             | m[((n >> 24) & 0XFF)]


#r = FastReverse()
#val = 43261596
#print bin(val)
#print (r.reverseBits(val))

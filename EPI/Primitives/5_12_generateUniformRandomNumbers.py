import sys
import os
import re
import math
import random

"""
    =============================================================================
    Implement a random number generator that generates a random integer i between
    a and b, inclusive, given a random number generator that produces either zero
    or one with equal probability. All generated values should be equally likely
    =============================================================================


    Solution:

    Note that it's easy to produce a random number greater than or equal to 0 and
    less than a power of 2, say 2^i - we just concatente i bits produced by the
    random number generator. For example, two calls to the random number generator
    produce (00)2, (01)2, (10)2, (11)2 and all of these are equally likely. These
    four possible outcomes encode the four integers 0, 1, 2, 3.

    For general case, first note that it's equivalent to product a random integer
    between 0 and b - a, inclusive, since we can simply add a to the result. Let
    t = b - a + 1, add i be the least integer such that t < 2^i. If t = 2^i, we 
    use the appraoch in the previous paragraph. If t is not a power of 2, the i calls
    may or may not encode an integer in the range 0 to t - 1. If the number is in
    the range, we return it; since all the numbers are equally likely, the result is
    correct. If the number is outside the range [0, t - 1], we keep trying until we
    do get a number in [0, t - 1]. For example, if t = 3, we might product 01 on the
    first try, in which case we return 1. If instead we product (11)2, wihch is outside
    the range [0, 2], we try again


    Time complexity:
    To understand the running time, first observe that the probability that it takes
    more than k calls is ((2^i - t)/2^i)^k, Since 2^i is the smalles pwoer of 2 greater
    than or equals to t, ((2^i - t)/2^i)^k < (1/2)^k. Hence the average number of calls
    is bounded by 1(1/2) + 2(1/2)^2 + 3(1/2)^3 + ..., which is:
        
        1/2 + 2/4 + 3/8 + 4/16 + ...

      = 1/2 + 1/4 + 1/8 + 1/16 + ... (= 1)
              1/4 + 1/8 + 1/16 + ... (= 1/2)
                    1/8 + 1/16 + ... (= 1/4)

                            ...

      = 1/2 + 1/4 + 1/8 + ...
      = 1/(1-1/2)
      = 2

      Hence on average two calls are needed to get the desired outcome
"""
def generator(a, b):
    assert( a <= b )

    if a <= b + 1:
        return a if a == b else a + zeroOneRandomGenerator()

    t = b - a + 1
    res = 0
    while True:
        res = 0
        i = 1
        while i < t:
            res = (res << 1) | zeroOneRandomGenerator()
            i <<= 1

        if res < t:
            break

    return res + a
        


def zeroOneRandomGenerator():
    return random.randrange(0, 2)

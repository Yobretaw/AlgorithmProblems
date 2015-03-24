import sys
import os
import re
import math

"""
    A brute-force appraoch is to iteratively substract y from x util the remaining term is
    less than y. The number of such substraction is exactly the quotient, x/y. The complexity
    of the brute-force appraoch is very high, e.g., when y = 1 and x = 2^31 - 1, it will take
    2 ^ 31 - 1 iterations

    A better appraoch is to try and get more work done in each iteration. For example, we can
    compute the largest k such that 2^k * y <= x, substract 2^k * y from x, and add 2^k to the
    quotient. To be concrete, if x = (1011)2 and y = (10)2, then k = 2. We substract (1000)2
    from (1011)2 to get (11)2, add (100)2 to the quotient, and continue by updating x to (11)2
"""
def divide(x, y):
    assert(y != 0)

    result = 0
    while x >= y:
        """
            This method leads to O(n^2) time complexity where n is the width of 
            x / y since we search the maximum value of k where 2^k * y <= x iteratively
        """
        #power = 1
        
        #while (y << power) >= (y << (power - 1)) and (y << power) <= x:
        #    power += 1

        #result += 1 << (power - 1)
        #x -= y << (power - 1)


        """
            This method leads to O(nlogn) time complexity where n is the width of 
            x / y. We binary search the maximum k such that 2^k * y <= x
        """
        k = binarySearchMax(x, y)
        result += 1 << k
        x -= y << k

    return result

def binarySearchMax(x, y):
    """
        find the largest k such that 2^k * y <= x
    """
    low = 0
    high = len(bin(x)) - 3

    while low < high:
        mid = low + (high - low) / 2 

        if (y << mid) <= x and (y << (mid + 1)) >= x:
            return mid
        elif (y << (mid + 1)) <= x:
            low = mid + 1
        else:
            high = mid

    return 0
    


#print divide(0, 0)
#print divide(1, 0)
#print divide(1, 1)


import sys
import os
import math
import random
import imp


"""
    The storge capacity of hand drives dwarfs that of RAM. This can lead to
    interesting space-time trade-offs

    Suppose you were given a file containing roughly one billion IP addresses,
    each of which is a 32-bit unsigned integer. How would you programmatically
    find an IP address that is not in file? Assume you have unlimited drive
    space but only a few megabytes of RAM at your disposal.

    =============

    Since the input is in a file, we can make multiple passes through it. We
    can use this to narrow the search down to subsets of the space of all IP
    addresses as follows. We make a pass through the file to count the number
    of IP addresses whose leading bit is 0. At least one IP address must exist
    which is not present in the file, so at least one of these two counts is
    below 2^31. For example, suppose we have determined using counting that
    there must be an IP address which begins with 0 that is absent from the
    file. We can focus our attention on IP addresses in the file that begins
    with 0, and coutinue the process of eliminiation based on the second bit.
    This entails 32 passes, and uses only two integer-valued count variables
    as storge.

    Since we have more storege, we can count on groups of bits. Specifically,
    we can count the number of IP addresses in the file that begin with 0, 1,
    2, ..., 2^16 - 1, using an array of 2^16 32-bit unsigned integers that 
    initialized to 0. For every IP address in the file, we take its 16 MSBs
    to index into this array and increment the count of that number. Since
    the file contains fewer than 2^32 numbers, there must be one entry in the
    array that is less than 2^16. This tells us that there is at least one IP
    address which has those upper bits which is not in file. In the second pass,
    we can focus only on the addresses whose leading 16 bits match the one we 
    have found, and use a bit array of size 2^16 to identify a missing address
"""
def find_missing_ip(file_name):
    arr = [0] * (1 << 16)
    for line in open(file_name):
        val = int(''.join(line.split('.')))
        idx = val >> 16
        arr[idx] += 1

    idx = -1
    for i, v in enumerate(arr):
        if v < (1 << 16):
            idx = i
            break
    
    assert(idx >= 0)
    arr = [0] * (1 << 16)
    for line in open(file_name):
        val = int(''.join(line.split('.')))
        if (val >> 16) == idx:
            arr[val & 0xFFFF] += 1

    for i, v in enumerate(arr):
        if v == 0:
            return idx << 16 + i

    return None

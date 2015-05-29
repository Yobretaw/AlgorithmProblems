import sys
import math

"""
    Count the number of prime numbers less than a non-negative number, n.
"""
def count_primes(n):
    if n <= 1:
        return 0

    arr = [True] * n
    arr[0] = arr[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not arr[i]: continue
        for j in range(2 * i, n, i):
            arr[j] = False
    return len(filter(lambda x: x, arr))


#print count_primes(2)
#print count_primes(3)
#print count_primes(5)

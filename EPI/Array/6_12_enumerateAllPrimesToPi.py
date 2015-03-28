import sys
import os
import re
import math

"""
    ============================================================================================
    Write a function that takes a single positive integer argument n(n >= 2) and return all the
    prime between 1 and n
    ============================================================================================

    Solution: specificaly, we use a bit array P to encode the set of primes. Initialize each entry
    to 1. When the algorithm finishes. the entry P[i] will be set to 0 if and only if i is not a
    prime. We initialize the iterator variable p to 2. We iterate over the multiples of p, setting
    the corresponding entries in P to 0 - these indices cannot be primes, since they are divisible
    by p. Then we update p to the next unmarked entry in p, and iterate.

    This runtime of approach can be improved somewhat by ignoring even numbers and not allocating
    entries for i less than 3. The count can also start from p^2 instead of p, since all numbers
    kp, where k < p have already been marked.


    We justified the sieving approach over the trial-division algorithm on heurisitic grounds.
    The time to sieve out the multiply of p is proportional to n/p, so the overall time complexity
    is O(n/2 + n/3 + n/5 + n/7 + ...) = O(nloglogn). The space complexity is O(n)
"""
def findPrimes(n):
    if n == 2:
        return 2

    primes = [2]
    kSize = (n - 3) / 2 + 1
    
    # is_prime[i] represents (2i + 3) is prime or not. Initially assuming
    # everyone is prime by setting to all of them to True
    is_prime = [True] * kSize

    for i in range(0, kSize):
        if is_prime[i]:
            p = (i * 2) + 3
            primes.append(p)

            # sieving from p^2, where p^2 = 4i^2 + 12i + 9 whose index in is_prime is
            # 2i^2 + 6i + 3 because is_prime[i] represents 2i + 3.
            for j in range(i**2 * 2 + 6 * i + 3, kSize, p):
                is_prime[j] = False

    return primes

print findPrimes(100)

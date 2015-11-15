import sys
import math

"""
     Write a program that determines a sequence of steps by which the required
     amount of milk can be obtained using the worn-out jugs. The milk is being
     added to a large mixing bowl, and hence cannot be removed from the bowl.
     Furthermore, it is not possible to pour one jug's contents into another.

     Your scheme should always work, i.e., return between 2100 and 2300 mL of
     milk, independent of how much is chosen in each individual step, as long
     as that quantity satisfies the given constraints.
"""
"""
    The time complexity is O((L + 1)(H + 1)n). The time directly spent within
    each call to determine_measure_sequence_help, except for the recursive
    call, is O(n), and because of the cache, there are at most (L + 1)(H + 1)
    calls to determine_measure_sequence_help. The space complexity is (L + 1)*
    (H + 1), which is the upper bound on the size of the cache.
"""
def determine_measure_sequence(jugs, l, h):
    cache = set()
    return determine_measure_sequence_help(jugs, l, h, cache)

def determine_measure_sequence_help(jugs, l, h, cache):
    if l > h or (l, h) in cache or l < 0 and h < 0:
        return False

    for j in jugs:
        if l <= j[0] and h >= j[1] or \
                determine_measure_sequence_help(jugs, l - j[0], h - j[1], cache):
            return True

    cache.add((l, h))
    return False


"""
    Variant 17.8.1

    Suppose jug i can be used to measure any quantity in [l_i, u_i] exactly.
    Determine if it is possible to measure a quantity of milk between L and H.
"""
def determine_measure_sequence2(jugs, l, h):
    cache = set()
    return determine_measure_sequence_help2(jugs, l, h, cache)

def determine_measure_sequence_help2(jugs, l, h, cache):
    if l > h or (l, h) in cache or l < 0 and h < 0:
        return False

    for j in jugs:
        if j[0] <= l <= j[1] or j[0] <= h <= j[1] or \
                determine_measure_sequence_help2(jugs, l - j[0], h - j[1], cache):
            return True

    cache.add((l, h))
    return False



if __name__ == '__main__':
    jugs = [(230, 240,), (290, 310, 500, 515)]

    print determine_measure_sequence(jugs, 2100, 2300)
    print determine_measure_sequence2(jugs, 2100, 2300)

    print determine_measure_sequence(jugs, 2790, 2920)
    print determine_measure_sequence2(jugs, 2790, 2920)

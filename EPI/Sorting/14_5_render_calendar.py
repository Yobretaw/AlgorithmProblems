import sys
import math
import itertools
import string
from collections import Counter


"""
    Given a list of events each specified by a (start_time, end_time) tuple.
    Compute the maximum number of events that take place concurrently.
"""
def max_concurrent_events(events):
    n = len(events)
    if n < 2:
        return n

    # sort all events by start time
    endpoints = [None] * (2 * n)
    for i, e in enumerate(events):
        endpoints[2 * i], endpoints[2 * i + 1] = (e[0], 0), (e[1], 1)

    endpoints.sort(key=lambda x : x[0])
    max_count = 0
    curr_count = 0
    for p in endpoints:
        if not p[1]:
            curr_count += 1
        else:
            curr_count -= 1
        max_count = max(max_count, curr_count)
    return max_count


"""
    Variant 14.5.1

    Users 1, 2, ..., share an Internet connection. User i uses b_i bandwidth
    from time s_i to f_i inclusive. What is the peak bandwidth usage?
"""
def peak_bandwidth_usage(b, s, f):
    n = len(b)
    if n < 2:
        return b[0] if n else 0

    
    endpoints = [None] * (2 * n)
    for i in range(n):
        # each entry in endpoints is a (index_in_b, start/end_time, is_end_bool)
        endpoints[2 * i] = (i, s[i], 0)
        endpoints[2 * i + 1] = (i, s[i], 1)

    def compare(a, b):
        return a[1] < b[1] if a[1] != b[1] else not a[2]

    endpoints.sort(cmp=compare)

    max_usage = 0
    curr_usage = 0
    for p in endpoints:
        if not p[1]:
            curr_usage += b[p[0]]
        else:
            curr_usage -= b[p[0]]
        max_usage = max(max_usage, curr_usage)

    return max_usage


if __name__ == '__main__':
    events = [
        (1, 5),
        (2, 7),
        (4, 5),
        (6, 10),
        (8, 9),
        (9, 17),
        (11, 13),
        (12, 15),
        (14, 15)
    ]
    print max_concurrent_events(events)

    events = [
        (0, 5),
        (2, 9),
        (6, 9),
        (8, 10)
    ]
    print max_concurrent_events(events)

    events = [(1, 20), (2, 8), (2, 22), (3, 15), (8, 12), (14, 17), (19, 20)]
    print max_concurrent_events(events)

import os
import math
import sys
from collections import defaultdict, Counter


"""
    A web server logs pages view in a log file. The log file consists of a line
    per page view. A page view consists of a page id and a user id, separated
    by a comma. The affinity of a pair of page is the number of distinct users
    who viewed both For example, in the log file below, the affinity of ayhoo
    and oogleg is 2.

    ayhoo, ap42
    oogleg, ap42
    tweeter, thl
    oogleg, aa314
    oogleg, aa314
    oogleg, thl
    tweeter, aa314
    tweeter, ap42
    ayhoo, aa314

    Write a function which takes as input a log file and returns a pair of pages
    which have the highest affinity.
"""
def find_highest_affinity_pair(page_views):
    # page_views is a list of string '<page>,<user>'
    n = len(page_views)
    if n < 2:
        return None

    # remove duplicates
    page_views = set(tuple(line.split(',')) for line in page_views)

    user_to_page = defaultdict(set)
    affinity = defaultdict(int)

    for page, user in page_views:
        if user in user_to_page:
            for _page in user_to_page[user]:
                if (page, _page) in affinity:
                    affinity[(page, _page)] += 1
                else:
                    affinity[(_page, page)] += 1
        user_to_page[user].add(page)

    return Counter(affinity).most_common(1)


page_views = [
    'ayhoo,ap42',
    'oogleg,ap42',
    'tweeter,thl',
    'oogleg,aa314',
    'oogleg,aa314',
    'oogleg,thl',
    'tweeter,aa314',
    'tweeter,ap42',
    'ayhoo,aa314'
]
print find_highest_affinity_pair(page_views)

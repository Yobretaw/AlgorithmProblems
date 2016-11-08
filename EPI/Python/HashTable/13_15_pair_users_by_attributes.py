import os
import math
import sys
from collections import defaultdict, Counter


"""
    You are given a sequence of users where each user has a unique 32-bit
    integer key and a set of attributes specified as strings. When you read
    a user, you should pair that user with another previously read user with
    identical attributes who is currently unpaired, if such user exists. If
    the user cannot be paired, you should add him to the unpaired set.
"""
def pair_users(users):
    # 'users' is a list of tuple (userId, set(str))

    # we assign a unique integer to each attribute
    count = 0
    attr2idx = {}
    for user in users:
        for a in user[1]:
            if not a in attr2idx:
                attr2idx[a] = count
                count += 1

    attr2user = {}
    res = []
    for uid, attrs in users:
        attr_tuple = tuple(attr2idx[a] for a in attrs)
        if attr_tuple in attr2user:
            attr2user.pop(attr_tuple)
            res.append((attr2user[attr_tuple], uid))
        else:
            attr2user[attrs] = uid

    return res

import sys
import math


"""
    You have n users with unique hash code h_0 through h_{n-1}, and m servers.
    The hash code are ordered by index, i.e., h_i < h_{i+1} for 0 <= i <= i - 2.
    User i requires b_i bytes of storage. The values k_0 < k_1 < ..., k_{m-2} are
    used to assign users to server. Specifically, the user with hash code c gets
    assigned to the server with the lowest ID i such that c <= k_i, or to Serve
    m - 1 if no such i exists, or to Server m - 1 if no such i exists. This re-
    stricted mapping of users to servers means that the user-to-server lookup
    can be implemented mapping of users to servers means that the user-to-server
    can be implemented with a BST on m - 1 nodes, rather than a hash table on n
    users. The load on a server is the sum of the bytes of storage of all users
    assigned to that server. Compute values for k_0, k_1, ..., k_{m-2} that minimize
    the load of the most heavily loaded server.

    ----

    Let L(p, q) be the maximum load on a server when users with hash code h_0
    through h_p are assigned to servers 0 and q in an optimum way, i.e., when
    the maximum load is minimized. The following recurrence holds:

        L(p, q) = min_{0 <= x <= p}(max(L(x, q - 1), sum_{x + 1 <= i <= p}b_i))

    In other words, to find the optimum assignment of users with hash codes h0
    though h_p to q servers, we find x such that if we assign the first x + 1
    users optimally to q - 1 servers and the remainder to server q, the maximum
    load on a given server is minimized.

    We can use the recurrence to tabulate the values in L till we get L(n - 1,
    m - 1). The base case corresponds to entries of the form L(p, 0), in which
    case the maximum load is sum_{0 <= i <= p}b_i. The time complexity to compute
    L(n - 1, m - 1) is O(n^2 * m)

    A qualitatively different approach, based on a greedy algorithm, is to check
    whether k_0, k_1, ..., k_{m - 2} can easily be done - iterate through the
    n users in the order of their hash code, and assign them to the servers
    greedily, i.e., assign users to servers, moving on the next server when the
    capacity of the current server is exceeded.

    We perform a binary search to get the minimum b, and the corresponding values
    for k_0, k_1, ..., k_{m - 2}. The time complexity of this approach is thus
    O(nlogW), where W is the sum of bytes of all users. This approach is much
    faster in practice.
"""

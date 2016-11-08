import sys
import math

"""
    You need to design a protective case. Specifically, the case can protect
    the enclosing device from a fall from up to some number of floors, and you
    want to determine what the number of floor is. You want to achieve this
    using no more than c cases. An additional constraint is that you can perform
    only d drops before the building supervisor stops you.

    You know that there exists a floor x such that the case will break if it is
    dropped from any floor x or higher but will remain intact if dropped from a
    floor below x. The ground floor is numbered zero, and it is given that the
    case will not break if dropped from the ground floor.

    Given c cases and d drops, what is the maximum number of floors that you can
    test in the worst case?

    -------------

    Let f(c, d) be the maximum number of floors we can test with c identical
    cases and at most d drops. We know that f(1, d) = d. Suppose we know the
    value of f(i, j) for all i <= c and j <= d.

    If we are given c + 1 cases and d drops we can start at floor f(c, d - 1)
    + 1 and drop a case. If the case breaks, then we can use the remaining
    c cases and d - 1 drops to determine the floor exacly, since it must be
    in the range [1, f(c, d - 1)]. If the case did not break, we proceed to
    floor f(c, d - 1) + 1 + f(c + 1, d - 1)

    Therefore f satifies the recurrence
        
            f(c + 1, d) = (f(c, d - 1) + 1) + f(c + 1, d - 1)
"""
# The time and space complexity are O((c + 1)(d + 1))
def determine_critical_height(c, d):
    f = [[-1 for i in range(d + 1)] for j in range(c + 1)]
    return determine_critical_height_help(f, c, d)

def determine_critical_height_help(f, c, d):
    if c == 0 or d == 0:
        return 0
    elif c == 1:
        return d
    else:
        if f[c][d] == -1:
            f[c][d] = determine_critical_height_help(f, c, d - 1) + \
                    determine_critical_height_help(f, c - 1, d - 1) + 1
        return f[c][d]


def determine_critical_height_iterative(c, d):
    f = [[0 for i in range(d + 1)] for j in range(c + 1)]

    # f(1, d) = 1 for all d
    for i in range(0, d + 1):
        f[1][i] = 1

    for i in range(1, c + 1):
        for j in range(0, d + 1):
            if i == 0 or j == 0:
                f[i][j] = 0
            else:
                f[i][j] = f[i][j - 1] + f[i - 1][j - 1] + 1

    return f[-1][-1]


"""
    Variant 17.13.1

    How would you compute the minimum number of drops needed to find the breaking
    point from 1 to F floors using c cases?
"""
# Time: O(nk^2), space O(nk)
def find_min_drop(F, c):
    # t[i][j] represents the minimum number of trials needed for i cases
    # and j floors
    t = [[0 for i in range(F + 1)] for j in range(c + 1)]

    # we need one trial for one floor and 0 trial for 0 floor
    for i in range(1, c + 1):
        t[i][1] = 1
        t[i][0] = 0

    # we always need j trials for one case and j floors
    for j in range(1, F + 1):
        t[1][j] = 1

    MAX_INT = sys.maxint
    for i in range(2, c + 1):
        for j in range(2, F + 1):
            t[i][j] = MAX_INT
            for k in range(1, j + 1):
                # Drop a case at kth floor. If it breaks, then the total number
                # of trials is one plus the number of trials required when having
                # i - 1 cases and dropping at (k - 1)th floor. If the case doesn't
                # break, then the total number of trials is one plus the number of
                # trials when having i cases and dropping at (j - k)th floor, as
                # we know it's safe to drop at all floors below and includes the kth
                # floor. Since we want to know the minimum number of trials in the
                # worst case, we take the maximum of the two.
                res = 1 + max(t[i - 1][k - 1], t[i][j - k])
                t[i][j] = min(t[i][j], res)

    return t[c][F]


if __name__ == '__main__':
    print determine_critical_height(4, 10)
    print determine_critical_height_iterative(4, 10)
    print find_min_drop(100, 9)

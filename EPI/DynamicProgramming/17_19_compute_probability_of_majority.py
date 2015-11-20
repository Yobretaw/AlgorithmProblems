import sys
import math


"""
    Assuming elections are statistically independent and that the probability
    of a Republican winning Election i is p_i, how would you compute the proba-
    bility of a Republican majority.

    -----

    Let Pr(r, n) be the probability that exactly r Republican win in elections
    {1, 2, ..., n}.

    Exactly r Republicans win in elections {1, 2, ..., n} if (1) r Republicans
    win in elections {1, 2, ..., n - 1} and the Republican candidate loses election
    n, or (2) r - 1 Republicans win in elections {1, 2, ..., n - 1} and the
    Republican candidate wins election n.

    Since these events are disjoint, Pr(r, n) is the sum of the probabilities of
    these two events. To be precise,

        Pr(r, n) = Pr(r - 1, n - 1)p_n + Pr(r, n - 1)(1 - p_n)

    Therefore P can be computed using DP; the base case for the recursion are
    Pr(0, 0) = 1 and Pr(r, n) = 0 for r > n.

    The complexity of computing Pr(i, j) for 0 <= i <= j <= n is proportional
    to the square of the number of elections.
"""
def compute_winning_prob(prob):
    n = len(prob)

    P = [[None for i in range(n + 1)] for j in range(n + 1)]

    prob_sum = 0.0
    for r in range(int(math.ceil(0.5 * n)), n + 1):
        prob_sum += compute_winning_prob_help(prob, r, n, P)
    
    return prob_sum

def compute_winning_prob_help(prob, r, n, P):
    if r > n:
        return 0.0
    elif r == 0 and n == 0:
        return 1.0
    elif r < 0:
        return 0.0

    if P[r][n] is None:
        P[r][n] = compute_winning_prob_help(prob, r - 1, n - 1, P) * prob[n - 1] + \
                compute_winning_prob_help(prob, r, n - 1, P) * (1.0 - prob[n - 1])

    return P[r][n]


if __name__ == '__main__':
    p = [0.5] * 100
    print compute_winning_prob(p)

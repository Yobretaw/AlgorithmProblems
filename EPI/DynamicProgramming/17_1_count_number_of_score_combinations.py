import sys
import math


"""
    You have an aggregate score k and W which specifies the points that can be
    scored in an individual play. How would you find the number of combinations
    of plays that result in an aggregate score of s? How would you compute the
    number of distinct sequences of individual plays that result in a score of
    s?
"""
def count_number_combination(k, scores):
    if not k or not scores:
        return 0

    n = len(scores)
    A = [[0 for i in range(k + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        A[i][0] = 1

    for i in range(1, n + 1):
        score = scores[i - 1]
        for j in range(score, k + 1):
            A[i][j] = A[i - 1][j] + (A[i][j - score] if j >= score else 0)

    return A[-1][-1]


def count_number_combination2(k, scores):
    combinations = [0] * (k + 1)
    combinations[0] = 1
    for score in scores:
        for j in range(score, k + 1):
            combinations[j] += combinations[j - score]
    return combinations[-1]


def count_permutation(k, scores):
    permutations = [0] * (k + 1)
    permutations[0] = 1
    for i in range(k + 1):
        for score in scores:
            if i >= score:
                permutations[i] += permutations[i - score]
    return permutations[-1]


"""
    Variant 17.1.1.

    Suppose the final score is given in the form (s, s'), i.e., Team 1 scores s
    and Team 2 scores s' points. How would you compute the number of distinct
    scoring sequences which result in this score?
    
    For example, if the final score is (6, 3), then team 1 scores 3, Team 2
    scores 3, Team 1 scores 3 is a scoring sequence which results in this
    final score.
"""
# Time: O(kmn) where k is the number of scores, m = len(s) and n = len(t)
def compute_scoring_sequence(scores, s, t):
    if not scores:
        return 0

    if not s and not t:
        return 1

    n = len(scores)

    # f[i][j] is the number of scoring sequences that yields i score for team
    # 1 and j score for team 2.
    f = [[0 for i in range(t + 1)] for j in range(s + 1)]
    f[0][0] = 1

    for score in scores:
        if score > s and score > t:
            break

        for sc in range(score, max(s + 1, t + 1), score):
            if sc <= s:
                f[sc][0] = 1
            if sc <= t:
                f[0][sc] = 1

    for i in range(1, s + 1):
        for j in range(1, t + 1):
            for score in scores:
                if score > i and score > j:
                    break
                if score <= i:
                    f[i][j] += f[i - score][j]
                if score <= j:
                    f[i][j] += f[i][j - score]

    return f[-1][-1]

"""
    Suppose the final score is (s, s'). How would you compute the maximum number
    of times the team that lead could have changed? For example, if s = 10 and
    s' = 6, the lead could have changed 4 times: Team 1 scores 2, then Team 2
    scores 3 (lead change), then Team 1 scores 2 (lead change), then Team 2 sc-
    ores 3 (lead change), then Team 1 scores 3 (lead change) followed by 3.
"""
#def compute_max_lead_change(scores, s, t):
#    if not scores:
#        return 0

#    if not s and not t:
#        return 1

#    n = len(scores)

#    # f[i][j] is the maximum number of lead changes given the final scoring (i, j)
#    f = [[0 for i in range(t + 1)] for j in range(s + 1)]
#    f[0][0] = 0

#    for score in scores:
#        if score > s and score > t:
#            break

#        for sc in range(score, max(s + 1, t + 1), score):
#            if sc <= s:
#                f[sc][0] = 1
#            if sc <= t:
#                f[0][sc] = 1

#    for i in range(1, s + 1):
#        for j in range(1, t + 1):
#            if i == j:
#                continue
#            for score in scores:
#                if score > i and score > j:
#                    break
#                if score <= i and i > j and i - score < j:
#                    f[i][j] = max(f[i][j], 1 + f[i - score][j])
#                if score <= j and i < j and j - score < i:
#                    f[i][j] = max(f[i][j], 1 + f[i][j - score])
#    return f[-1][-1]


if __name__ == '__main__':
    s = 12
    scores = [2, 3, 7]
    #print count_number_combination(s, scores)
    #print count_number_combination2(s, scores)
    #print count_permutation(s, scores)

    print compute_scoring_sequence([2, 3, 7], 14, 13)
    print compute_scoring_sequence([2, 3, 7], 10, 6)

    print compute_max_lead_change([2, 3, 7], 10, 6)

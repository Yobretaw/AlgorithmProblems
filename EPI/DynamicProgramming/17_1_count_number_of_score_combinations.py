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
        for j in range(1, k + 1):
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


if __name__ == '__main__':
    s = 12
    scores = [2, 3, 7]
    print count_number_combination(s, scores)
    print count_number_combination2(s, scores)
    print count_permutation(s, scores)

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


"""
    Variant 17.1.1.

    Suppose the final score is given in the form (s, s'), i.e., Team 1 scores s
    and Team 2 scores s' points. How would you compute the number of distinct
    scoring sequences which result in this score?
    
    For example, if the final score is (6, 3), then team 1 scores 3, Team 2
    scores 3, Team 1 scores 3 is a scoring sequence which results in this
    final score.
"""
def compute_scoring_sequence(scores, s, t):
    if not scores:
        return 0

    if not s and not t:
        return 1

    n = len(scores)

    # table[i][j][k] is the number of distinct scoring sequences that results
    # (j, k) score pair using the first i scores
    table = [[[0 for i in range(t + 1)] for i in range(s + 1)] for k in range(n + 1)]

    for i in range(n + 1):
        table[i][0][0] = 1

    for j in range(s + 1):
        for k in range(t + 1):
            for i in range(1, n + 1):
                score = scores[i - 1]
                table[i][j][k] = table[i - 1][j][k]

                for idx in reversed(range(i - 2, i)):
                    sc = scores[idx]
                    if j >= sc:
                        table[i][j][k] += table[i][j - sc][k]
                    if k >= sc:
                        table[i][j][k] += table[i][j][k - sc]

                #if j >= score:
                #    table[i][j][k] += table[i][j - score][k]
                
                #if k >= score:
                #    table[i][j][k] += table[i][j][k - score]

                print i, j, k, '   curr: ', table[i][j][k], '  prev: ', table[i - 1][j][k]

    #for i in range(1, n + 1):
    #    score = scores[i - 1]
    #    print score
    #    for j in range(0, s + 1):
    #        for k in range(0, t + 1):
    #            table[i][j][k] = table[i - 1][j][k]

    #            if score > j and score > k:
    #                print i, j, k, '   curr: ', table[i][j][k], '  prev: ', table[i - 1][j][k]
    #                continue

    #            if j >= score:
    #                table[i][j][k] += table[i][j - score][k]

    #            if k >= score:
    #                table[i][j][k] += table[i][j][k - score]

    #            #for idx in reversed(range(i)):
    #            #    sc = scores[idx]
    #            #    if j >= sc:
    #            #        table[i][j][k] += table[i][j - sc][k]
    #            #    if k >= sc:
    #            #        table[i][j][k] += table[i][j][k - sc]

    #            print i, j, k, '   curr: ', table[i][j][k], '  prev: ', table[i - 1][j][k]

    return table[-1][-1][-1]


#def compute_scoring_sequence2(scores, s, t):
#    res = [0]
#    indices = [0, 0]
#    accu = [0, 0]

#    compute_scoring_sequence2(scores, s, t, indices, accu, res)
#    return res

#def compute_scoring_sequence2(scores, s, t, indices, accu, res):
#    if indices[0] == s and indices[1] == t:
#        res[0] += 1
#        return
#    elif indices[0] > s or indices[1] > t:
#        return



if __name__ == '__main__':
    s = 12
    scores = [2, 3, 7]
    #print count_number_combination(s, scores)
    #print count_number_combination2(s, scores)
    #print count_permutation(s, scores)

    print compute_scoring_sequence([2, 3, 7], 4, 3)

import sys
import os
import imp
import math
from collections import defaultdict

from BST import Node, bst_print, generate_complete_bst


"""
    Student test scores are recorded in a file. Each line consists of a student
    ID, which is an alphanumberic string, and an integer between 0 and 100, in-
    clusive.

    Write a function which takes as input the name of the file containing n test
    scores and outputs the student who has the maximum average score across all
    his or her top three tests. If the student has fewer than three test scores,
    discard that student. Return 'no such student' if no student has three or
    more test scores.
"""
def find_max_average_scores(lines):
    id2scores = defaultdict(list)

    for line in lines:
        line = line.split(' ')
        sid, score = line[0], int(line[1])

        id2scores[sid].append(score)
        id2scores[sid] = sorted(id2scores[sid], reverse=True)[:3]

    res = 'no such student'
    max_score = 0
    for sid, scores in id2scores.items():
        if len(scores) == 3 and sum(scores) > max_score:
            res = sid
            max_score = sum(scores)

    return res


if __name__ == '__main__':
    lines = [
        'Allen 99',
        'Bob 89',
        'Chris 95',
        'Allen 97',
        'Bob 88',
        'Chris 98',
        'Allen 96',
        'Bob 99',
        'Chris 98',
        'Zed 50'
    ]
    print find_max_average_scores(lines)

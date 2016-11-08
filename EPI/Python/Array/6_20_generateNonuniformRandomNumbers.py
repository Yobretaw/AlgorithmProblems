import sys
import os
import re
import math
import random

"""
    ============================================================================================
    You are given n real numbers t_0, t_1, ..., t_n-1 and probabilities p_0, p_1, ..., p_n-1, 
    which sums to 1. Given a random number generator that produces values in [0, 1] uniformlly,
    how would you generate a number in T according to the specified probabilities?
    ============================================================================================
"""
def randomSelect(T, P):
    P_accu = [P[0]]

    for i in range(1, len(P)):
        P_accu.append(P[i] + P_accu[i - 1])

    r = random.random()
    
    for i in range(0, len(P_accu)):
        if r < P_accu[i]:
            return T[i]


T = [0, 1, 2, 3]
P = [0.1, 0.2, 0.3, 0.4]
#P = [0.25,0.25,0.25,0.25]

count = [0] * 4
for i in range(0, 10000):
    count[randomSelect(T, P)] += 1
print count

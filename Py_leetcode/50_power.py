import sys
import math
from collections import defaultdict

"""
    Implement pow(x, n).
"""
def power(x, n):
    is_neg = 1 if n < 0 else 0
    n = max(n, -n)

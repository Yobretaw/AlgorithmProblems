import sys
import math
from heapq import *
from collections import OrderedDict

"""
    Design an algorithm for efficiently computing the k smallest real numbers
    of the form a + b * sqrt(2) for nonnegative integers a and b.
"""
# Brute force. Time: O(k^2 * logk)
def compute_numbers(k):
    if not k:
        return []

    a = b = 0
    res = [(0, 0)]
    sqrt_2 = math.sqrt(2)

    q = [(a + b * sqrt_2, (a, b)) for a in range(0, k - b) for b in range(0, k)]
    q.sort(key=lambda x: x[0])
    return [e[1] for e in q[:k]]

"""
    It is wasteful to generate k^2 numbers as almost all of which are discarded.
    We know the smallest number is 0 + 0 * sqrt_2. The candidate for next smallest
    number are 1 + 0 * sqrt_2 and 0 + 1 * sqrt_2. From this, we can deduce that
    the following algorithm. We want to maintain a collection of real numbers,
    initialized to 0 + 0 * sqrt_2. We perform k extractions of the smallest element,
    call it a + b * sqrt_2, followed by insertion of (a + 1) + b * sqrt_2 and a + 
    (b + 1) * sqrt_2 to the collection. We can use induction to prove that the
    i-th element extracted is the i-th smallest number of the form a + b * sqrt_2.
    
    This algorithm runs in O(klogk) time.
"""
def compute_numbers2(k):
    if not k:
        return []

    res = OrderedDict()
    q = [(0, (0, 0))]
    sqrt_2 = math.sqrt(2)
    while len(res) < k:
        a, b = heappop(q)[1]
        res[(a, b)] = None

        if (a + 1, b) not in res:
            heappush(q, (a + 1 + b * sqrt_2, (a + 1, b)))
        if (a, b + 1) not in res:
            heappush(q, (a + (b + 1) * sqrt_2, (a, b + 1)))

    return res.keys()


"""
    Now we describe an O(k) time solution. We incrementally build the result array
    'res'. The key idea is that the (n + 1)-th entry in res will be the sum of 1 or
    sqrt_2 with a previous entry. We could iterate through the first n entries in
    'res' and track the smallest value of the form A[i] + 1 or A[i] + sqrt_2, which
    is greater than res[n - 1]a However this takes O(n) time to compute the (n + 1)-th
    element.

    Instead we trakc just two elements, i and j. Specifically,  we track the smallest
    i such that res[i] + 1 > res[n - 1] and the smallest j such that res[j] + sqrt_2 >
    res[n - 1]. Then res[n] is the smaller of res[i] + 1 and res[j] + sqrt_2. If res[n]
    is assigned res[i] + 1 we increment i. If res[i] is assigned res[j] + sqrt_2, we
    increment j. If res[i] + 1 = res[j] + sqrt_2, we increment both.
"""
class Num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2)

def compute_numbers3(k):
    if not k:
        return []

    res = []
    res.append(Num(0, 0))
    i = j = 0
    for p in range(k):
        x = Num(res[i].a + 1, res[i].b)
        y = Num(res[j].a, res[j].b + 1)

        if x.val < y.val:
            i += 1
            res.append(x)
        elif x.val > y.val:
            j += 1
            res.append(y)
        else:
            i += 1
            j += 1
            res.append(x)

    return [(num.a, num.b) for num in res]


if __name__ == '__main__':
    k = 10
    l1 = compute_numbers(k)
    l2 = compute_numbers2(k)
    l3 = compute_numbers3(k)

    for i in range(k):
        print l1[i], l2[i], l3[i]

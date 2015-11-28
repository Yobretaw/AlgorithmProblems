import sys
import math


"""
    Given a array of integers, find the element that appears more than half of
    all elements.
"""
def find_majority(A):
        n = len(A)
        if not n:
            return None

        res = None
        count = 0
        for v in A:
            if v == res:
                count += 1
            elif count > 0:
                count -= 1
            else:
                res = v
                count = 1

        return res if count > 0 else None


if __name__ == '__main__':
    A = [1, 1, 2, 3, 1, 2, 2, 2, 2, 2]
    A = [1, 2, 3]
    print find_majority(A)

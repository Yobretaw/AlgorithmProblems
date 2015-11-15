import sys
import math

"""
    Design an algorithm for the knapsack problem that selects a subset of items
    that has maximum value and weights at most w onces. All items have integer
    weights and values.
"""
def maximize_value(w, weights, values):
    n = len(weights)

    t = [0] * (w + 1)
    for i in range(n):
        for j in reversed(range(weights[i], w + 1)):
            t[j] = max(t[j], t[j - weights[i]] + values[i])
    return t[-1]


def maximize_value2(w, weights, values):
    n = len(weights)

    t = [0] * (w + 1)
    d = [[(0, 0) for i in range(w + 1)] for j in range(n)]
    for i in range(n):
        for j in range(weights[i]):
            d[i][j] = (-1, 0)
        for j in reversed(range(weights[i], w + 1)):
            if t[j] > t[j - weights[i]] + values[i]:
                t[j] = t[i - 1][j]
                d[i][j] = (-1, 0)
            else:
                t[j] = t[j - weights[i]] + values[i]
                d[i][j] = (-1, -weights[i])
    #t = [[0 for i in range(w + 1)] for j in range(n)]
    #d = [[(0, 0) for i in range(w + 1)] for j in range(n)]
    #for i in range(n):
    #    for j in range(0, w + 1):
    #        if j < weights[i] or t[i - 1][j] > t[i - 1][j - weights[i]] + values[i]:
    #            t[i][j] = t[i - 1][j]
    #            d[i][j] = (-1, 0)
    #        else:
    #            t[i][j] = t[i - 1][j - weights[i]] + values[i]
    #            d[i][j] = (-1, -weights[i])

    res = []
    i, j = n - 1, w
    while i >= 0 and j >= 0:
        left, up = d[i][j]
        if up:
            res.append((weights[i], values[i]))
        i, j = i + left, j + up
    
    return res


"""
    Variant 17.7.1

    Solve the knapsack problem when the theif can take a factorial amount of
    items.
"""
def maximize_value_fraction(w, weights, values):
    if not w or not weights or not values:
        return 0

    arr = [(float(a[0]) / a[1], a[0], a[1]) for a in zip(weights, values)]
    arr.sort(key=lambda x: x[0])

    accu_weight = 0
    accu_value = 0
    for ratio, weight, value in arr:
        curr = min(w - accu_weight, weight)
        if not curr:
            break

        accu_value += curr / ratio
        accu_weight += curr
    return accu_value


if __name__ == '__main__':
    weights = [20, 8, 60, 55, 40, 70, 85, 25, 30, 65, 75, 10, 95, 50, 40, 10]
    values = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
    print maximize_value(130, weights, values)
    print maximize_value2(130, weights, values)
    print maximize_value_fraction(130, weights, values)

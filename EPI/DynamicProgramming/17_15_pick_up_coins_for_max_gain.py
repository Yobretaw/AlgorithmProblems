import sys
import math


"""
    In a pick-up-coin game, an even number of coins are placed in a line. Two
    players, F and S, take turns at choosing one coin each - they can only
    choose from the two coins at the ends of the line. Player F goes first.
    The game ends when all coins have been picked up. The player whose coins
    have the higher total value wins. A player cannot pass his turn.

    Design an efficient algorithm for computing the maximum margin of victory
    for the starting player in the pick-up-coins game.
"""
# This algorithm computes the maximum difference F can get, i.e., how much higher
# F can get over S.
def max_gain(coins):
    n = len(coins)
    return max_gain_help(coins, 0, n - 1, {})


def max_gain_help(coins, l, r, d):
    # if l + r is odd, it's F's turn, S's turn otherwise.
    if l == r:
        return coins[l] if (l + r) & 1 else -coins[l]

    if (l, r) in d:
        return d[(l, r)]

    take_left = max_gain_help(coins, l + 1, r, d)
    take_right = max_gain_help(coins, l, r - 1, d)

    if (l + r) & 1:
        # F is trying to maximize the difference against S
        d[(l, r)] = max(coins[l] + take_left, coins[r] + take_right)
    else:
        # S is trying to minimize the difference against F
        d[(l, r)] = min(-coins[l] + take_left, -coins[r] + take_right)

    return d[(l, r)]


# This algorithm compute the maximum number of coins F can get
def max_gain2(coins):
    n = len(coins)
    t = [[-1 for i in range(n)] for j in range(n)]

    return max_gain_help2(coins, 0, n - 1, t)

def max_gain_help2(coins, a, b, t):
    if a > b:
        return 0

    if t[a][b] == -1:
        # maximize F's gain
        t[a][b] = max(
                coins[a] + min(max_gain_help2(coins, a + 2, b, t),         # F, S both take left
                               max_gain_help2(coins, a + 1, b - 1, t)),    # F takes left, S takes right
                coins[b] + min(max_gain_help2(coins, a + 1, b - 1, t),     # F takes right, S takes left
                               max_gain_help2(coins, a, b - 2, t))         # F, S both take right
                )
    return t[a][b]
 
if __name__ == '__main__':
    coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]
    #coins = [1, 2, 3, 4]
    #coins = [1, 2, 3, 4, 5, 6]
    print max_gain(coins)
    print 2 * max_gain2(coins) - sum(coins)

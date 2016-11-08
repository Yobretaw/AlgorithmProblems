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
    # the last coin is always picked by S.
    if l == r:
        return -coins[l]

    if (l, r) in d:
        return d[(l, r)]

    take_left = max_gain_help(coins, l + 1, r, d)
    take_right = max_gain_help(coins, l, r - 1, d)

    # if l + r is odd, it's F's turn, otherwise it's S's turn.
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

def max_gain_help2(coins, l, r, t):
    if l > r:
        return 0

    if t[l][r] == -1:
        # maximize F's gain
        t[l][r] = max(
                coins[l] + min(max_gain_help2(coins, l + 2, r, t),         # F, S both take left
                               max_gain_help2(coins, l + 1, r - 1, t)),    # F takes left, S takes right
                coins[r] + min(max_gain_help2(coins, l + 1, r - 1, t),     # F takes right, S takes left
                               max_gain_help2(coins, l, r - 2, t))         # F, S both take right
                )
    return t[l][r]


"""
    Variant 17.15.1

    You are given two fixed arrays of numbers A and B, each of length k, and
    another array C, also of length k. You can assign C[i] to one of A[i], B[i],
    or 0, subject to the constraint that if C[i] = A[i] then C[i - 1] must be
    assigned to 0 if i > 0.

    Design an efficient algorithm that computes an assignment to C that maximize
    the sum of the elements in C.
"""
def max_assigments(A, B):
    n = len(A)
    d = {}

    return max_assigments_help(A, B, n - 1, d)

# This helper function retunrs the maximum poissible sum of C[0 ... idx]
def max_assigments_help(A, B, idx, d):
    if idx < 0:
        return 0

    if idx == 0:
        return max(A[0], B[0], 0)

    if idx in d:
        return d[idx]

    take_A_idx = A[idx] + max_assigments_help(A, B, idx - 2, d)
    not_take_A_idx = max(B[idx], 0) + max_assigments_help(A, B, idx - 1, d)

    d[idx] = max(take_A_idx, not_take_A_idx)
    return d[idx]


"""
    Variant 17.15.2

    The DP algorithm above given above has O(n^2) time complexity. Suppose the
    objective is relaxed, and the goal is simply not to lose. Assuming the
    number of coins is even, design a more efficient algorithm for the starting
    player.
"""
def not_loose(coins):
    pass


"""
    Variant 17.15.2

    In the one red card game, a deck of 52 playing cards is shuffled and placed
    face-down on a table. To win, you must select a red card. You can either
    examine or select the top card. If you choose examine, the top card is reve-
    aled and discarded. If you choose select, the game ends - you win if it is a
    red card and lose otherwise. After examing 51 cards, you must select the last
    card.

    Note there are 26 red cards and 26 black cards in total.

    Design a strategy that maximize the probability of winning at the one red
    card game.
"""
def compute_winning_strategy(cards):
    # card in the back of 'cards' is the top card in the table
    pass


"""
    In the multibet card color game, a deck of 52 playing cards is shuffled and
    placed face-down on a table. You can bet on the color of the top card at
    even odds. After you have placed your bet, the top card is revealed to you
    and discarded. Betting comtinues till the deck is exhausted. Suppose you
    are playing the multibet card color game and are restricted to bet in penny
    increments. Compute a tight lower bound on the amount that you can guarantee
    to win.
"""
def compute_tight_bound():
    pass

 
if __name__ == '__main__':
    #coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]
    #print max_gain(coins)
    #print 2 * max_gain2(coins) - sum(coins)

    #coins = [1, 2, 3, 4]
    #print max_gain(coins)
    #print 2 * max_gain2(coins) - sum(coins)

    #coins = [1, 2, 3, 4, 5, 6]
    #print max_gain(coins)
    #print 2 * max_gain2(coins) - sum(coins)

    #A = [1, 2, 3, 4]
    #B = [2, 1, 3, 5]
    #print max_assigments(A, B)

    pass

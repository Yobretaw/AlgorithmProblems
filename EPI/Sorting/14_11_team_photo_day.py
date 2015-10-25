import sys
import math


"""
    You are a photographer for a soccer meet. You will be taking pictures of
    pairs of opposing teams. All teams have the same number of players. A team
    photo consists of a front row of players and a back row of players. A player
    in the back row must be taller than the player in from of him. All players
    in a row must be from the same team.
    
    Design an algorithm that takes as input two teams and the heights of the
    players in the teams and checks if it is possible to place players to take
    the photo subject to the placement constraint.
"""
def arrange_players(t1, t2):
    n = len(t1)
    if n < 2:
        return None if not n else [(min(t1[0], t2[0]), max(t1[0], t2[0]))]
    
    t1.sort()
    t2.sort()

    if t1[0] >= t2[0]:
        t2, t1 = t1, t2

    for i in range(n):
        if t1[0] < t2[0]:
            continue
        else:
            return None
    return [(t1[i], t2[i]) for i in range(n)]


if __name__ == '__main__':
    pass


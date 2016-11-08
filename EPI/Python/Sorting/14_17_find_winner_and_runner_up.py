"""
    There are 128 players participating in a tennis tournament. Assume that the
    "x beats y" relationship is transitive i.e for all players A, B and C if A
    beats B and B beats C, then A beats C.
    
    What is the least number of matches we need to organize to find the best
    player? How many matches do you need to find the best and the second best
    player?

    ==========


    First we consider the problem of finding the best player. Each game
    eliminates one player and there are 128 players; so 127 matches are
    necessary and sufficient.

    To find the second best player, note that the best player have played
    7 matches, thus we can find the second best player by organizing 6
    matches between the 7 players who lost to the best players, for a total
    of 127 + (7 - 1) = 133 matches.

    Generalizing to k players, k - 1 games are needed to find the best player,
    and then ceiling(logk) - 1 additional games must be played to find the
    second best, i.e., a total of k + ceiling(logk) - 2 games are needed to
    find the best player and the runner-up.
"""

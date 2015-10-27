import sys
import os


"""
    You are the coach of a cycling team with 25 members and need to determine
    the fastest, second-fastest, and third-fastest cyclists for selection to
    the Olympic team.

    Let number of matches played till now be matchCount = 0;

    Lets us name the players as Ai, Bi, Ci, Di and Ei where 1 <= i <= 5

     GROUP 1	  GROUP 2	  GROUP 3	  GROUP 4	GROUP 5
       A1           A2              A3	            A4	          A5
       B1           B2              B3	            B4	          B5
       C1           C2              C3	            C4	          C5
       D1           D2              D3	            D4	          D5
       E1           E2              E3	            E4	          E5

    Now in 5 different matches we get the 5 winners from each of the groups.
    Without the loss of generality we can assume that winners are A1, A2, A3,
    A4 and A5 ( Bi and Ci for 1<=i  <= 5 at 2nd and 3rd position).

    matchCount = 5

    Now lets have a race among A1, A2, A3, A4 and A5.

    matchCount = 5 + 1 = 6

    Now without any loss of generality we can assume A1 to be the winner and
    A2 & A3 be at second and third position respectively. So if A1 is the winner
    then closest to A1 in race would be B1, C1, A2 and A3. Having another race
    will reveal the players at 2nd and 3rd position.

    machCount = 6 + 1 = 7

    So in 7 matches we can identify the players at 2nd and 3rd position
"""

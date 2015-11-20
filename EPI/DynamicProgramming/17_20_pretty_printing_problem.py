import sys
import math


"""
    Given text, i.e., a string of words separated by single blanks, decompose
    the text into lines such that no word in split across lines and the mess-
    iness of the decomposition is minimized. Each line can hold no more than L
    characters. How would you change your algorithm if the messiness is the sum
    of the messinesses of all but the last line?

    Note: the messiness of a line ending with b blank characters is 2^b. The
    total messiness of a sequence of lines is the sum of messinesses of all the
    lines.
"""
def optimize_decomposition(words, L):
    n = len(words)

    # M[i] is the optimized messiness of words[:i]
    M = [sys.maxint] * (n + 1)

    # calculating M[i]
    for i, word in enumerate(words):
        b_len = L - len(word)
        M[i] = (M[i - 1] if i >= 1 else 0) + 1 << b_len

        # Iterating from j = i + 1 down to the first f such that len(words[i + 1]) + 
        # Sum_{k = f to i}(len(words[k]) + 1) > L.
        for j in reversed(range(0, i)):
            b_len -= (len(words[j]) + 1)

            if b_len < 0:
                break

            M[i] = min((M[j - 1] if j >= 1 else 0) + (1 << b_len), M[i])

    # Finds the minimum cost without considering the last line
    # If the last line is <w_j, w_{j + 1}, ..., w_i}, the optimal messiness will
    # be M[j - 1]
    min_mess = (M[n - 2] if n >= 2 else 0)
    b_len = L - len(words[-1])
    for i in reversed(range(0, n - 1)):
        b_len -= (len(words[i]) + 1)

        if b_len < 0:
            return min_mess

        min_mess = min(min_mess, (0 if i < 1 else M[i - 1]))

    return min_mess

if __name__ == '__main__':
    s = 'I have inserted a large number of new examples from the papers for the Mathematical Tripos during the last twenty years, which should be useful to Cambridge students.'
    print optimize_decomposition(s.split(' '), 36)

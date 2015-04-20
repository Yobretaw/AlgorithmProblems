import sys
import math

"""
    Determine whether an integer is a palindrome. Do this without extra space.

    Some hints:
    Could negative integers be palindromes? (ie, -1)

    If you are thinking of converting the integer to string, note the restriction of using extra space.

    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
    you know that the reversed integer might overflow. How would you handle such case?

    There is a more generic way of solving this problem.
"""
def palindrome_number(x):
    if x < 10:
        return False if x < 0 else True

    m = 1
    while m * 10 < x:
        m *= 10

    while x > 0:
        if x / m != x % 10:
            return False
        
        x = (x % m) / 10
        m /= 100

    return True

#print palindrome_number(-1)
#print palindrome_number(12321)

print p

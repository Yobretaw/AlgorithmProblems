import os
import math
import sys
from collections import defaultdict, Counter

"""
    You are required to write a method which takes text for an anonymous letter
    and text for a maganize. Your method is to determine if it is possible to
    write the anonymous letter using the text from the maganize. The anonymous
    letter can be written from the maganize if for each character whether the
    number of times it appears in the anonymous letter is less than or equal
    to the number of times it appears in the maganize.
"""
def determine_constructible(letter, text):
    if not letter:
        return True

    c1 = Counter(letter)
    c2 = Counter(text)

    for c, n in c1.iteritems():
        if not c in c2 or n > c2[c]:
            return False

    return True

#letter = 'methhodd'
#text = 'meethodd'
#print determine_constructible(letter, text)


#letter = 'methhodd'
#text = 'meethhodd'
#print determine_constructible(letter, text)

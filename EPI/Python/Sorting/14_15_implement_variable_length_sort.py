import sys
import os


"""
    Most sorting algorithms rely on a basic swap step. When records are of
    different lengths, the swap step becomes nontrival.

    A text file is read into an array of characters with null characters
    indicating the line boundaries. Write a program that takes as input
    such an array, and prints the lines in sorted order. The array corresponds
    to a large number of lines, and while most lines are short, some are very
    long.
"""
def sort_lines(lines):
    """
        Use 'indirect sort': build an array of references to the records. Then
        sort the references using the compare function on the referenced records.
    """
    pass

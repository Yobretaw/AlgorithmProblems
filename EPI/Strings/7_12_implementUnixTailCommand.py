import sys
import os
import re
import math

"""
    ============================================================================================
    The UNIX 'tail' command displays the last part of a file. For this problem, assume that tail
    takes two arguments - a file name, and the number of lines, starting from the last line, that
    are to be printed.

    Implement the UNIX 'tail' command
    ============================================================================================
"""
def tail(fname, n):
    """
        Print the last n lines of the file 'fname'
    """
    try:
        f = open(fname, 'r')
    except IOError:
        print "IOError: No such file or directory: '" + fname + "'"
        return
    
    # NOT IMPLEMENTED...
    f.close()

import sys
import os
import math

from stack import Stack

"""
    ============================================================================================
    A file or a directory can be specified via a string called the pathname. This string may
    specify an absolute path, starting from the root, e.g. /usr/bin/gcc, or a path relative
    to the current working directory, e.g., scripts/awkscripts.

    The same directory may be specified by multiple directory paths. For example,
    /usr/lib/../bin/gcc and scripts//./../scripts/awkscripts/././ specify equivalent absolute
    and relative pathnames.

    Write a function which takes a pathname, and returns the shortest equivalent pathname. Assume
    individual directories and files have names that use only alphanumberic characters. Subdirectory
    names may be combined using forward slashed('/'), the current directory '.' and the parent
    directory '..'
    ============================================================================================
"""
def shortest_path(path):
        if not path:
            return ""

        p = path.split('/')
        s = Stack()

        for d in p:
            if d == '.' or d == '':
                pass
            elif d == '..':
                if not s.empty():
                    s.pop()
            else:
                s.push(d)

        l = []
        while not s.empty():
            l.append(s.top())
            s.pop()

        l[:] = l[::-1]

        if path[0] == '/':
            # absolute path
            return '/' + '/'.join(l)
        else:
            # relative path
            return '/'.join(l)


#print shortest_path('/usr/lib/../bin/gcc')
#print shortest_path('scripts//./../scripts/awkscripts/././')
#print shortest_path('/../')             # -> '/'
#print shortest_path('/..')              # -> '/'
#print shortest_path('/abc/...')         # -> '/abc/...'

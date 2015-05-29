import sys
import math
from collections import defaultdict
from set import Set

"""
    There are a total of n courses you have to take, labeled from 0 to n - 1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
    which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

    For example:

    2, [[1,0]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

    2, [[1,0],[0,1]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take
    course 0 you should also have finished course 1. So it is impossible.

    Note:
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about
    how a graph is represented:

        - https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

    Hints:
    This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological
    ordering exists and therefore it will be impossible to take all courses.

    Topological Sort via DFS

    Topological sort could also be done via BFS.
"""
def can_finish(num_courses, prereq):
    if num_courses < 2:
        return True
    
    path = defaultdict(list)
    for c in prereq:
        path[c[0]].append(c[1])

    searched = set()
    for start in path.keys():
        if not dfs(path, set(), start, searched):
            return False
    return True

def dfs(path, seen, curr, searched):
    if curr in searched:
        return True

    for x in path[curr]:
        if x in seen:
            return False

        seen.add(x)
        if not dfs(path, seen, x, searched):
            return False

        seen.remove(x)
    searched.add(curr)
    return True

#arr = [[1, 0], [0, 1]]
#print can_finish(2, arr)

import sys
import math
from collections import defaultdict

"""
    There are a total of n courses you have to take, labeled from 0 to n - 1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

    There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

    For example:

    2, [[1,0]]

    There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

    4, [[1,0],[2,0],[3,1],[3,2]]

    There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be
    taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
"""
def find_order(num_courses, prereq):
    if not num_courses or not prereq:
        return [c for c in range(0, num_courses)]

    relation = defaultdict(list)
    for c in prereq:
        relation[c[1]].append(c[0])

    res = []
    searched = {}
    for start in relation.keys():
        if not dfs(relation, start, set(), searched, res):
            return []

    return res[::-1] + [c for c in range(0, num_courses) if not c in res]


def dfs(relation, curr, seen, searched, res):
    if curr in seen:
        return False
    if curr in searched:
        return True

    seen.add(curr)
    for x in relation[curr]:
        if not dfs(relation, x, seen, searched, res):
            return False

    searched[curr] = 1
    seen.remove(curr)
    res.append(curr)
    return True


#num = 2
#arr = [[1, 0]]
#arr = [[1, 0], [0, 1]]
#print find_order(num, arr)
#print find_order(4, [[1,0],[2,0],[3,1],[3,2]])
#print find_order(3, [[2, 0], [2, 1]])
#print find_order(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])

import sys
import os
import imp
import math

from BST import Node, \
        bst_print, \
        generate_complete_bst, \
        bst_insert_node, \
        bst_remove_node, \
        bst_get_leftmost, \
        bst_get_rightmost


"""
    You are given a set of line segments. Each segment consists of a closed
    interval [l_i, r_i] of the x-axis, a color, and a height (y-coordinate).
    When viewed from above, the color at the point x on the x-axis is the
    color of the highest segment that includes x.

    Implement a function that computes the view from above. Your input is a
    sequence of n line segments, each specified as 4-tuple <l, r, c, h>,
    where l and r are the left and right endpoint, respectively, c encodes
    the color, and h are the height. The output should be in the same format.
    No two segment whose intervals overlap have the same height.
"""
class LineSegment:
    def __init__(self, left, right, color, height):
        self.left, self.right = left, right
        self.color = color
        self.height = height

    def __repr__(self):
        return '[%s:%s, %s](%s)' % (self.left, self.right, self.height, self.color)

class Endpoint:
    def __init__(self, is_left, seg):
        self.is_left = is_left
        self.seg = seg

    def value(self):
        return self.seg.left if self.is_left else self.seg.right

    def __le__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __repr__(self):
        return 'is_left:%s' % str(self.is_left) + ' ' + self.seg.__repr__()


def compute_view_from_above(segments):
    n = len(segments)
    if n < 2:
        return [] if not n else list(segments)

    endpoints = [Endpoint(True, seg) for seg in segments]
    endpoints.extend([Endpoint(False, seg) for seg in segments])
    endpoints.sort()

    root = None
    prev = None
    prev_xaxis = endpoints[0].value()
    root = None
    for p in endpoints:
        if root and prev_xaxis != p.value():
            right_most_node = bst_get_rightmost(root)
            if prev == None:
                prev = LineSegment(
                            prev_xaxis,
                            p.value(),
                            right_most_node.store.color,
                            right_most_node.store.height
                            )
            else:
                if prev.height == right_most_node.store.height and \
                        prev.color == right_most_node.store.color:
                    prev.right = p.value()
                else:
                    print prev
                    prev = LineSegment(
                            prev_xaxis,
                            p.value(),
                            right_most_node.store.color,
                            right_most_node.store.height
                            )

        prev_xaxis = p.value()

        if p.is_left:
            root = bst_insert_node(root, p.seg.height, p.seg)
        else:
            root = bst_remove_node(root, p.seg.height)
        #print '-' * 100
        #bst_print(root)

    if prev:
        print prev


if __name__ == '__main__':
    segments = [
        LineSegment(0, 4, 'bottomright', 1),
        LineSegment(1, 3, 'bottomleft', 3),
        LineSegment(2, 7, 'dot', 2),
        LineSegment(4, 5, 'doubleLine', 4),
        LineSegment(5, 7, 'singleLine', 1),
        LineSegment(6, 10, 'bottomright', 3),
        LineSegment(8, 9, 'bottomright', 2),
        LineSegment(9, 18, 'verticalLine', 1),
        LineSegment(11, 13, 'singleLine', 3),
        LineSegment(12, 15, 'verticalLine', 2),
        LineSegment(14, 15, 'dot', 3),
        LineSegment(16, 17, 'singleLine', 3)
    ]
    compute_view_from_above(segments)

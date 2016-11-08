import sys
import os
import re
import math
import random

"""
    Write a function that tests if two rectangles have a non-empty intersection.

    If the intersection is nonempty, return the rectangle formed by their
    intersection
"""
class Rectangle():
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y

        self.width = width
        self.height = height


def intersectRectangle(r, s):
    if isIntersect(r, s):
        return Rectangle(
                max(r.x, r.x),
                max(r.y, s.y),
                min(r.x + r.width, s.x + s.width) - max(r.x, s.x),
                min(r.y + r.height, s.y + s.height) - max(r.y, s.y)
                )
    else:
        return Rectangle(0, 0, -1, -1)


def isIntersect(r, s):
    return (
            r.x <= s.x + s.width and 
            s.x <= r.x + r.width and
            r.y <= s.y + s.height and
            s.y <= r.y + r.height
           )


"""
    Variant 5.13.1: Given four points in the plane, write a function to determine if
    these four points form a rectangle
"""
class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

def isRectangle(a, b, c, d):
    v1 = (a.x - b.x, a.y - b.y)
    v2 = (b.x - c.x, b.y - c.y)
    v3 = (c.x - d.x, c.y - d.y)
    v4 = (d.x - a.x, d.y - e.y)

    f = lambda a, b: a.x * b.x + a.y * b.y

    arr = [v1, v2, v3, v4]
    for i in range(0, len(arr)):
        if not f(arr[i], arr[(i + 1) % len(arr)]):
            return False

    return True

"""
    Variant 5.13.2: Write a function that checks whether two rectangles, not necessarily
    aligned with the X and Y axes, intersect?
"""

class Rectangle2:
    def __init__(self, points):
        self.points = []

        if points:
            self.points.extend(points)

def isIntersect2(r, s):
    for rec in [r, s]:
        for i in len(rec.points):
            p1 = rec.points[i]
            p2 = rec.points[(i + 1) % len(r.points)]

            normal = Point(p2.y - p1.y, p1.x - p2.x)
            minA = None
            maxA = None
            for p in r.points:
                projected = normal.x * p.x + normal.y * p.y
                if minA == None or projected < minA:
                    minA = projected
                if maxA == None or projected > maxA:
                    maxA = projected
                    
            minB = None
            maxB = None
            for p in s.points:
                projected = normal.x * p.x + normal.y * p.y
                if minB == None or projected < minB:
                    minB = projected
                if maxB == None or projected > maxB:
                    maxB = projected

            if maxA < minB or maxB < minA:
                return False

    return True

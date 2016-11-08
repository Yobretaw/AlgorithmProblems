import sys
import os
import math
import imp

from stack import Stack

"""
    ============================================================================================
    A queue can be implemented using an array and two additional fields, the beginning and end
    indices. This structure is sometimes reffered to as a circular queue. Both 'enqueue' and
    'dequeue' takes constant time. If the array is fixed, there is a maximum number of entries
    that can be stored. If the array is dynamically resized, the total time for m combined
    'enqueue' and 'dequeue' operations is O(m)

    Implement a queue API using an array for storing elements. Your API should include a constructor
    function, which takes as argument the capacity of the queue, 'enqueue' and 'dequeue' functions,
    a size function, which returns the number of elements stored, and implement dynamical resizing.
    ============================================================================================
"""
class Queue():
    def __init__(self, size=0):
        self._queue = [None] * size
        self._head = 0
        self._tail = 0
        self._count = 0

    def enqueue(self, val):
        n = len(self._queue)
        if self._count == n:
            old_queue = self._queue
            self._queue = []

            for i in range(self._head, n):
                self._queue.append(old_queue[i])

            if self._tail <= self._head:
                for i in range(0, self._tail):
                    self._queue.append(old_queue[i])

            self._queue.extend([None] * n)
            self._head = 0
            self._tail = n
            n *= 2

        self._tail = self._tail % n
        self._queue[self._tail] = val
        self._tail += 1
        self._count += 1

    def dequeue(self):
        if self._count == 0:
            return None

        res = self._queue[self._head]
        self._head = (self._head + 1) % len(self._queue)
        self._count -= 1
        return res

    def size(self):
        return self._count


#q = Queue(10)
#for i in range(0, 10):
#    q.enqueue(i)

#for i in range(0, 5):
#    q.dequeue()

#for i in range(0, 10):
#    q.enqueue(i)

#for i in range(0, q.size()):
#    print q.dequeue()

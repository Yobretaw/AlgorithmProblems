import sys
import math


"""
    Given n tasks and the corresponding time required to execute each task,
    compute an order in which to process tasks that minimizes the total waiting
    time.
"""
def min_waiting_time(times):
    times.sort()

    total = 0
    accu = times[0]
    for i in range(1, len(times)):
        total += accu
        accu += times[i]

    return total


if __name__ == '__main__':
    times = [3, 2, 6, 4, 9, 7]
    print min_waiting_time(times)

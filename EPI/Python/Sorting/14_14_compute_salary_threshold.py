import sys
import os
import math


"""
    You are working in the finance office for ABC corporation. ABC needs to
    cut payroll expenses to a specific target. The CEO wants to do this by
    putting a cap on last year's salaries. Every employee who earned more than
    the cap last year will be paid the cap this year; employees who earned no
    more than the cap will see no change in their salary.

    For example, if there were five employees with salaries last year being
    $90, $30, $100, $40, and $20, and the target payrol this year is 210, then
    $60 is a suitable salary cap, since 60 + 30 + 60 + 40 + 20 = 210.

    Design an algorithm for computing the salary cap, giving existing salaries
    and the target payroll.
"""
def compute_salary_cap(salaries, target):
    n = len(salaries)
    if n < 2:
        return 0 if not n else min(salaries[0], target)

    salaries.sort()
    total = salaries[0]
    for i in range(1, n):
        if total + (n - i) * salaries[i - 1] < target \
                and total + (n - i) * salaries[i] >= target:
            return int(float(target - total) / (n - i))
        total += salaries[i]
    return int(target / n)


if __name__ == '__main__':
    salaries = [90, 30, 100, 40, 20]
    print compute_salary_cap(salaries, 210)

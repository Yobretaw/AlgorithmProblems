import re

"""
    Implement a basic calculator to evaluate a simple expression string.

    The expression string contains only non-negative integers, +, -, *, /
    operators and empty spaces. The integer division should truncate towards
    zero.

    You may assume that the given expression is always valid.

    Some examples:

        "3+2*2" = 7
        " 3/2" = 1
        " 3+5 / 2 " = 5
"""
def calculate(s):
    if not s or len(s) < 2:
        return 0 if not s else int(s[0])

    s = s.replace(' ', '')
    st = []

    i = 0
    while i < len(s): 
        c = s[i]
        if c in ['*', '/']:
            num, i = next_int(s, i + 1)
            st.append(eval_str(st.pop(), c, num))
        elif c in ['+', '-']:
            st.append(c)
            i += 1
        else:
            num, i = next_int(s, i)
            st.append(num)

    res = 0
    i = 0
    while i < len(st):
        if st[i] not in ['+', '-']:
            res += int(st[i])
            i += 1
        else:
            res = eval_str(res, st[i], int(st[i + 1]))
            i += 2
    return res

def next_op(s, i):
    while i < len(s) and s[i].isdigit():
        i += 1
    return s[i] if i < len(s) else None

def next_int(s, i):
    num = 0
    while i < len(s) and s[i].isdigit():
        num = 10 * num + int(s[i])
        i += 1
    return num, i

def eval_str(l, op, r):
    return {
        '+': lambda x,y: x + y,
        '-': lambda x,y: x - y,
        '*': lambda x,y: x * y,
        '/': lambda x,y: x / y
    }[op](l, r)



def calculate2(s):
    n = p = 0
    ops = [None, None]
    args = [0, 0]

    ops[0] = '+'
    args[0] = 0
    for c in s:
        if c.isspace():
            continue

        if c in ['+', '-' ,'*', '/']:
            # if previous operator has first privilege
            if ops[p] in ['*', '/']:
                n = eval_str(args[p], ops[p], n)
                p -= 1
            
            if c in ['+', '-']:
                args[p] = eval_str(args[p], ops[p], n)
                ops[p] = c
            else:
                args[p + 1] = n
                ops[p + 1] = c
                p += 1
            n = 0
        else:
            n = n * 10 + int(c)

    if ops[p] in ['*', '/']:
        n = eval_str(args[p], ops[p], n)

    return eval_str(args[0], ops[0], n)


if __name__ == '__main__':
    # s = '3+2*2'
    # print calculate(s)
    # print calculate(" 3+5 / 2 ")
    # print calculate(" 32+5 / 2 ")
    # print calculate("14-13/2")
    # print calculate("0-2147483647")
    # print calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024")
    print calculate2("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024")

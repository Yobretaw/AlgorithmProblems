import re
"""
    Implement a basic calculator to evaluate a simple expression string.

    The expression string may contain open ( and closing parentheses ), the plus
    + or minus sign -, non-negative integers and empty spaces.

    You may assume that the given expression is always valid.

    Some examples:

        "1 + 1" = 2
        " 2-1 + 2 " = 3
        "(1+(4+5+2)-3)+(6+8)" = 23
"""
def calculate(s):
    if len(s) < 2:
        return 0 if not s else int(s[0])

    # remove white spaces
    s = list(s.replace(' ', ''))

    # stack to store op
    st = []
    ops = []
    curr = 0
    for i, c in enumerate(s):
        if c == '(':
            if i > 0:
                st.append(s[i - 1])
                curr += (0 if s[i - 1] == '+' else 1)
        elif c == ')':
            if st:
                op = st[-1]
                curr -= (0 if op == '+' else 1)
                st.pop()
        elif c == '+' or c == '-':
            ops.append(curr)

    # revert ops if needed
    count = 0
    for i, c in enumerate(s):
        if c == '+' or c == '-':
            if ops[count] % 2 == 1:
                s[i] = '+' if c == '-' else '-'
            count += 1

    res = 0
    op = None
    val = 0
    s = ''.join(s).replace('(', '').replace(')', '')
    for c in s:
        if c == '+' or c == '-':
            if op:
                res += val * (1 if op == '+' else -1)
            else:
                res += val
            op = c
            val = 0
        else:
            val = 10 * val + int(c)
    res = res + val * (1 if op != '-' else -1)
    return res

if __name__ == '__main__':
    print calculate("1 + 1")
    print calculate(" 2-1 + 2 ")
    print calculate("(1+(4+5+2)-3)+(6+8)")
    print calculate("2-(1-(4+5+2)-3)+(6+8)")
    print calculate("(5-(1+(5)))")

import sys
import os
import math

"""
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, /. Each operand may be an integer or another expression.

    Some examples:
      ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
      ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
def evalRPN(s):
    n = len(s)
    if n < 2:
        return int(s[0]) if n else 0

    st = []
    for c in s:
        try:
            st.append(int(c))
        except:
            second = st[-1]
            first = st[-2]
            st.pop()
            st.pop()
            st.append(evalHelp(first, second, c))
    return st[-1]

def evalHelp(a, b, op):
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(1.0 * x / y)
    }[op](a, b)


#print evalRPN(["2", "1", "+", "3", "*"])
#print evalRPN(['3', '-4', '+'])
#print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
#print evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])

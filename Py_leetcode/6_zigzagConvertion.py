import sys
import math

"""
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
    this: (you may want to display this pattern in a fixed font for better legibility)
    
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
    
    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
    
    *****************************************************************************
    
    n = 4
    
    P     I      N
    A   L S    I G
    Y A   H  R
    P     I
    
    n = 5
    
    P      H
    A    S I
    Y  I   R
    P L    I G
    A      N
    
    所以，对于每一层主元素坐标 (i,j) = (j + 1) * n + i
    对于每两个主元素之间的插入元素，(j + 1) * n - i
"""
def convert(s, nRows):
    if nRows == 1:
        return s

    n = len(s)
    result = ""
    for i in range(0, nRows):
        j = 0
        index = i
        while index < n:
            # main elements
            result += s[index]

            if i != 0 and i != nRows - 1:
                if index + (nRows - i - 1) * 2 < n:
                    # skewed elements
                    result += s[index + (nRows - i - 1) * 2]

            j += 1
            index = (2 * nRows - 2) * j + i

    return result

print convert("PAYPALISHIRING", 3)

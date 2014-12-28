#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

bool isNumeric(char c);

/* Implement atoi to convert a string to an integer.
 * 
 * Requirements:
 * - The function first discards as many whitespaces as necessary
 *   until the first non-whitespaces char is found. Then starting
 *   from this char, takes an optional initial plus or minus sign
 *   followed by as many numerical digits as possible, and inteprets
 *   them as numerical value.
 *
 * - The string can contain additional chars after those that form
 *   the integer number, which are ignored and have no effect on
 *   the behavior of this function
 *
 * - If the first sequence of non-whitespace chars in input is not
 *   a valid integral number, or if no such sequence exits because
 *   either str is empty or it contains only whitespace chars, no
 *   conversion is performed.
 *
 * - If no valid conversion could be performed, a zero value is
 *   returned. If the correct value is out of the range of repre-
 *   sentable values, INT_MAX or INT_MIN is returned.
 */
int atoi2(string s) {
  int len = s.length();

  int idx = 0;
  long long val = 0;
  int sign = 1;

  // first ignore any whitespaces in the front.
  while(s[idx] == ' ') idx++;

  // take optional sign
  if(s[idx] == '+' || s[idx] == '-') {
    if(s[idx++] == '-') sign = -1;
  }

  // invalid input
  if(!isNumeric(s[idx])) return val;

  // process numerical digits
  while(idx < len && isNumeric(s[idx])) {
    int currDigit = s[idx] - '0';
    val = val * 10 + sign * currDigit;

    // detect overflow
    if(val > INT_MAX) return INT_MAX;
    else if(val < INT_MIN) return INT_MIN;
    else idx++;
  }

  return val;
}

bool isNumeric(char c) {
  return '0' <= c && c <= '9';
}

int main() {
  string s = "2147483648";
  cout << atoi2(s) << endl;
  return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

/* Given a string containing just the characters '(' and ')', find
 * the length of the longest valid(well-formed) parentheses substring.
 *
 * For "(()", the longest valid parentheses is "()", which has length of 2
 *
 * Another example is ")()())", where the longest valid parentheses is "()()",
 * which is of length 4
 */
int longestValidParentheses(string s) {
  if(s.length() == 0 || s.length() == 1)
    return 0;

  int max_len = 0, last = -1; // position of the last ')'
  stack<int> lefts; // keep track of the positions of non-matching '('

  for (int i = 0; i < s.length(); ++i) {
    if(s[i] == '(') {
      lefts.push(i);
    } else {
      if(lefts.empty()) {
        last = i;
      } else {
        lefts.pop();
        if(lefts.empty())
          max_len = max(max_len, i - last);
        else
          max_len = max(max_len, i - lefts.top());
      }
    }
  }

  return max_len;
}

int main() {
  cout << longestValidParentheses("(()") << endl;
  cout << longestValidParentheses(")()())") << endl;
  cout << longestValidParentheses("()(()") << endl;
  cout << longestValidParentheses("(()") << endl;
  cout << longestValidParentheses("()(())") << endl;
  return 0;
}

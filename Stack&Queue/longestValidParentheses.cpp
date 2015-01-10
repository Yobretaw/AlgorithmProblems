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

  /* There are two cases that result a invalid string:
   * either extra '(' or extra ')'.
   * 
   * We use a stack to keep track the positions of '(' that
   * have not been matched yet, and use 'last' to track the 
   * extra ')' in the string.
   */
  int max_len = 0, last = -1; 
  stack<int> lefts;

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


// DP.
int longestValidParentheses_DP(string s) {
  if(s.length() == 0 || s.length() == 1)
    return 0;

  int max_len = 0;

  /* f[i] is the length of valid parentheses starting
   * from index i.
   */
  vector<int> f(s.size(), 0);
  for (int i = s.size() - 2; i >= 0; --i) {

    // match is the first unmatched ')' after index i
    int match = i + f[i + 1] + 1;

    // case: "((...))"
    if(s[i] == '(' && match < s.size() && s[match] == ')') {
      f[i] = f[i + 1] + 2;

      // if a valid sequence exist afterward "((...))()"
      if(match + 1 < s.size()) f[i] += f[match + 1];
    }
    max_len = max(max_len, f[i]);
  }
  return max_len;
}


// Time & Space: O(1)
int longestValidParentheses2(string s) {
  if(s.length() == 0 || s.length() == 1)
    return 0;

  int max_len = 0, depth = 0, start = -1;
  for (int i = 0; i < s.length(); ++i) {
    if(s[i] == '(') {
      depth++;
    } else {
      depth--;
      if(depth < 0) {
        start = i;
        depth = 0;
      } else if(depth == 0) {
        max_len = max(max_len, i - start);
      }
    }
  }

  depth = 0;
  start = s.size();
  for(int i = s.length() - 1; i >= 0; --i) {
    if(s[i] == ')') {
      depth++;
    } else {
      depth--;
      if(depth < 0) {
        start = i;
        depth = 0;
      } else if(depth == 0) {
        max_len = max(max_len, start - i);
      }
    }
  }

  return max_len;
}

int main() {
  cout << longestValidParentheses2("(()") << endl;
  cout << longestValidParentheses2(")()())") << endl;
  cout << longestValidParentheses2("()(()") << endl;
  cout << longestValidParentheses2("()(())") << endl;
  return 0;
}

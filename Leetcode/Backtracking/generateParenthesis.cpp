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

/*
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 * 
 * For example, given n = 3, a solution set is:
 * 
 *   "((()))", "(()())", "(())()", "()(())", "()()()"
 */
void genHelp(int n, int open, int close, string s, vector<string>& result) {
  if(open + close == 2 * n) {
      result.push_back(s);

    return;
  }

  if(open < n)
    genHelp(n, open + 1, close, s + '(', result);

  if(close < open)
    genHelp(n, open, close + 1, s + ')', result);
}

vector<string> generateParentheses(int n) {
  vector<string> result;
  genHelp(n, 0, 0, "", result);
  return result;
}

int main() {
  int n = 3;
  vector<string> result = generateParentheses(n);
  for (int i = 0; i < result.size(); ++i) {
    cout << result[i] << endl;
  }
  return 0;
}

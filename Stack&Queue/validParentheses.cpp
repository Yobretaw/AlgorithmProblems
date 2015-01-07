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

/* Given a string containing just the characters ')', ')', '{', '}',
 * '[' and ']', determine if the input string is valid.
 *
 * The brackets must close in the corrent order, '()', '{}' and '[]'
 * are all valid but '(]' and '([)]' are not valid.
 */
bool isValid(const string& s) {
  stack<char> brackets;
  for (int i = 0; i < s.length(); ++i) {
    char c = s[i];
    if(c == '(' || c == '{' || c == '[') {
      brackets.push(c);
    } else {
      if(brackets.empty() ||
          (brackets.top() == '(' && c != ')') ||
          (brackets.top() == '[' && c != ']') ||
          (brackets.top() == '{' && c != '}')) return false;
      brackets.pop();
    }
  }
  return brackets.empty();
}


// recursive method
bool isValid2(string s) {
  if (s.length() == 0)
    return true;
  else{
    string::size_type position = s.find("()");
    if (position == s.npos)
      position = s.find("[]");
    if (position == s.npos)
      position = s.find("{}");
    if (position != s.npos)
      return isValid2(s.erase(position, 2));
  }
  return false;
}

int main() {
  string s = "()";
  cout << isValid2(s) << endl;
  return 0;
}

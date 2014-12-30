#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

/* Write a function to find the longest common prefix string
 * amongst an array of strings
 */
string longestCommonPrefix(const vector<string>& strs) {
  if(strs.size() == 0)
    return "";

  string prefix = strs[0];
  int len = prefix.length();
  for (int i = 1; i < strs.size(); ++i) {
    if(prefix.length() > strs[i].length())
      len = min((int)strs[i].length(), len);

    for (int j = 0; j < len; ++j) {
      if(prefix[j] != strs[i][j]) {
        len = j;
        break;
      }
    }
  }

  return prefix.substr(0, len);
}


int main() {
  vector<string> strs = {
    "aba",
    "c",
    "b",
    "a",
    "ab"
  };

  cout << longestCommonPrefix(strs) << endl;
  return 0;
}


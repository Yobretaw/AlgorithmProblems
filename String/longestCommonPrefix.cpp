#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;


string lcp2(const vector<string>& strs) {
  if(strs.size() == 0) return "";
  
  string prefix = strs[0];
  for (int i = 0; i < prefix.length(); ++i)
    for (int j = 1; j < strs.size(); ++j)
      if(strs[j][i] != prefix[i]) return prefix.substr(0, i);

  return prefix;
}

/* Write a function to find the longest common prefix string
 * amongst an array of strings
 */
string lcp(const vector<string>& strs) {
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
    "a",
    "ab"
  };

  //cout << longestCommonPrefix(strs) << endl;
  cout << lcp2(strs) << endl;
  return 0;
}


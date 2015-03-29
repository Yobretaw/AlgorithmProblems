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
 *  Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
 *  
 *  For example, given s = "leetcode", dict = ["leet", "code"].
 *  
 *  Return true because "leetcode" can be segmented as "leet code".
 */
// Time: O(n^3)
bool canBreak(string s, const vector<string>& dict) {
  int n = s.length();

  unordered_map<string, bool> m;
  for(auto s : dict) m[s] = true;

  if(n == 0 || n == 1) return m[s];
  
  // mem[i][j] = 1 iff s[i..j] is in dict
  vector<vector<bool> > mem(n, vector<bool>(n, false));

  for (int i = 0; i < n; ++i)
    mem[i][i] = m[string(s, i, 1)];

  for(int len = 2; len <= n; ++len) {
    for(int start = 0; start <= n - len; ++start) {
      int end = start + len - 1;
      
      if(m[s.substr(start, len)]) {
        mem[start][end] = true;
        continue;
      }

      for (int mid = start; mid < end; ++mid) {
        mem[start][end] = mem[start][mid] && mem[mid + 1][end];

        if(mem[start][end]) break;
      }
    }
  }
  return mem[0][n - 1];
}

// Time: O(n^2)
bool canBreak2(string s, const vector<string>& dict) {
  int n = s.length();

  unordered_map<string, bool> m;
  for(auto s : dict) m[s] = true;

  if(n == 0 || n == 1) return m.count(s);

  vector<bool> mem(n + 1, false);
  mem[0] = true;

  for (int i = 1; i <= n; ++i)
    for(int j = i - 1; j >= 0; --j)
      if(mem[i] = (mem[j] && m.count(s.substr(j, i - j)))) break;

  return f[n];
}

int main() {
  string s = "ab";
  vector<string> dict = {"a", "b"};
  cout << canBreak(s, dict) << endl;
  return 0;
}

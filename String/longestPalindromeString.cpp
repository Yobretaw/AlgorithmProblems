#include "iostream"
#include "string"
#include "stdlib.h"
#include "vector"
using namespace std;

// Machester Algorithm
// Runtime: O(n)
// Space: O(n)
string longestPalSubstring(string s) {
  if(s.length() < 2) return s;

  string str = "#";
  for(int i = 0; i < s.length(); ++i) {
    str += s[i];
    str += "#";
  }

  int n = str.length();
  int f[n];
  int mid = 0, right = 0, pos = 0, len = 1;
  for(int i = 1; i < n; ++i) {
    if(right > i)
      f[i] = min(f[2 * mid - i], right - i);
    else
      f[i] = 0;

    while(i - f[i] - 1 >= 0 &&
          i + f[i] + 1 < n &&
          str[i - f[i] - 1] == str[i + f[i] + 1])
      f[i]++;

    if(len < f[i]) {
      len = f[i];
      pos = (i - f[i]) / 2;
    }
    if(right < i + f[i]) {
      mid = i;
      right = i + f[i];
    }
  }
  return s.substr(pos, len);
}

// DP
// Runtime: O(n^2)
// Space: O(n^2)
string lps(string s) {
  int len = s.length();
  vector<vector<int> > mem(len, vector<int>(len, 0));

  for(int i = 0; i < len; i++) {
    mem[i][i] = 1;
  }

  for(int i = 0; i < len - 1; i++) {
    mem[i][i+1] = (s[i] == s[i+1]);
  }

  for(int k = 3; k <= len; k++) {
    for(int start = 0; start <= len - k; start++) {
      int end = start + k - 1;
      mem[start][end] = (s[start] == s[end] && mem[start + 1][end - 1]);
    }
  }

  int maxlen = 0;
  int start, end;
  string result = "";
  for(int i = 0; i < len; i++) {
    for(int j = 0; j < len; j++) {
      if(mem[i][j] && ((j - i) > maxlen)) {
        maxlen = j - i;
        start = i;
        end = j;
      }
    }
  }
  return s.substr(start, end - start + 1);
}

int main()
{
  string s = "HHHeHHHelleoWorld";
  //string s = "babcbabcbaccba";
  cout << longestPalSubstring(s) << endl;
  cout << lps(s) << endl;
  return 0;
}

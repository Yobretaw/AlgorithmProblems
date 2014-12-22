#include "iostream"
#include "string"
#include "stdlib.h"
#include "vector"
using namespace std;

string preProcess(string s) {
  string ret = "#";
  for(int i = 0; i < (int)s.length(); i++) {
    ret += s[i];
    ret += "#";
  }

  return ret;
}

// Machester Algorithm
// Runtime: O(n)
// Space: O(n)
string longestPalSubstring(string s) {
  if(s.length() == 0)
    return "";

  s = preProcess(s);
  
  int currCenter = 0;
  int maxCenter = 0;
  int maxRadius = 0;
  int rightEnd = 0;

  int p[s.length()];
  memset(p, 0, sizeof(p));

  for(int i = 0; i < (int)s.length(); i++) {
    p[i] = (rightEnd > i)
      ? min(p[2 * currCenter - i], rightEnd - i)
      : 1;

    while(s[i + p[i]] == s[i - p[i]])
      p[i]++;

    if(i + p[i] > rightEnd) {
      rightEnd = i + p[i];
      currCenter = i;
    }

    if(p[i] > maxRadius) {
      maxCenter = i;
      maxRadius = p[i];
    }
  }

  if(maxRadius <= 2)
    return "";

  string ret = "";
  for(int i = maxCenter - maxRadius + 2; i <= maxCenter + maxRadius - 2; i+=2)
    ret += s[i];

  return ret;
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

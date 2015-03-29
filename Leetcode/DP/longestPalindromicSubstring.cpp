#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <climits>
using namespace std;


string lps(string s) {
  if(s.empty())
    return "";

  int n = s.length();
  int begin = 0;
  int maxlen = 1;
  vector<vector<int> > table(n, vector<int>(n));

  // base case: len 1
  for(int i = 0; i < n; i++) {
    table[i][i] = 1;
  }

  // base case: len 2
  for(int i = 0; i < n - 1; i++) {
    if(s[i] == s[i+1]) {
      table[i][i+1] = 1;
      begin = i;
      maxlen = 2;
    }
  }

  for(int len = 3; len <= n; len++) {
    for(int i = 0; i < n - len + 1; ++i) {
      int j = i + len - 1;
      if(s[i] == s[j] && table[i+1][j-1] == 1) {
        table[i][j] = 1;
        begin = i;
        maxlen = len;
      }
    }
  }

  return s.substr(begin, maxlen);
}


int main()
{
  string a = "aabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebabaabeddeeddebababeddeeddebababeddeeddebaba";
  cout << lps(a) << endl;
  return 0;
}

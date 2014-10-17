#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;


// Return the longest commmon substring of two string
// with length m and n respectively
// 
// Time complexity: O(m * n)
// Space: min(m, n)
string longestCommmonSubstr(const string& a, const string& b) {
  if(a.empty() || b.empty()) {
    return "";
  }

  string s = a.length() < b.length() ? a : b;
  string l = a.length() >= b.length() ? a : b;
  
  int maxLen = 0;
  int maxEnd = 0;
  int* curr = new int[s.length()];
  int* prev = new int[s.length()];

  for (int i = 0; i < l.length(); i++) {
    for (int j = 0; j < s.length(); j++) {
      if(l[i] != s[j]) {
        curr[j] = 0;
      } else {
        curr[j] = (i == 0 || j == 0) ? 1 : prev[j - 1] + 1;
      
        if(maxLen < curr[j]) {
          maxLen = curr[j];
          maxEnd = j;
        }
      }
    }

    swap(curr, prev);
  }
  
  delete curr;
  delete prev;
  return s.substr(maxEnd - maxLen + 1, maxLen);
}

int main()
{
  string a = "helloworld";
  string b = "lloworab";
  cout << longestCommmonSubstr(a, b) << endl;
  return 0;
}


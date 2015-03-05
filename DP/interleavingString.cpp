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
 * Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
 * 
 * For example, given:
 *    s1 = "aabcc",
 *    s2 = "dbbca",
 * 
 * When s3 = "aadbbcbcac", return true.
 * When s3 = "aadbbbaccc", return false.
 */
bool isInterleaving(const string s1, const string s2, const string s3) {
  int len1 = s1.length();
  int len2 = s2.length();
  int len3 = s3.length();

  if(len3 != len1 + len2) return false;
  if(len1 == 0) return s2 == s3;
  if(len2 == 0) return s1 == s3;

  // mem[i][j] is true if s1[1, i] and s2[1, j] is interleaving with
  // s3[1, i + j]
  //
  // Hence
  //    mem[i][j] =
  //      s1[i - 1][j] == s3[i + j - 1] && mem[i - 1][j]
  //     or
  //      s1[i][j - 1] == s3[i + j - 1] && mem[i][j - 1]
  vector<vector<int> > mem(len1 + 1, vector<int>(len2 + 1, 1));

  for (int i = 1; i <= len1; ++i) {
    mem[i][0] = (s1[i - 1] == s3[i - 1]) && mem[i - 1][0];
  }

  for (int i = 1; i <= len2; ++i) {
    mem[0][i] = (s2[i - 1] == s3[i - 1]) && mem[0][i - 1];
  }

  for (int i = 1; i <= len1; ++i) {
    for (int j = 1; j <= len2; ++j) {
      mem[i][j] = (s1[i - 1] == s3[i + j - 1] && mem[i - 1][j]) ||
                  (s2[j - 1] == s3[i + j - 1] && mem[i][j - 1]);
    }
  }
  return mem[len1][len2];
}

int main() {
  string s1 = "aabcc";
  string s2 = "dbbca";
  cout << isInterleaving(s1, s2, "aadbbcbcac") << endl;
  cout << isInterleaving(s1, s2, "aadbbbaccc") << endl;
  cout << isInterleaving("a", "", "c") << endl;
  cout << isInterleaving("aacaac", "aacaaeaac", "aacaaeaaeaacaac") << endl;
  return 0;
}

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
 *  Given a string S and a string T, count the number of distinct subsequences of S that are equal to T
 *  
 *  A subsequence of a string is a new string which is formed from the original string by deleting
 *  some (can be none) of the characters without disturbing the relative positions of the remaining
 *  characters. (i.e, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
 *  
 *  Here is an example:
 *  S = "rabbbit", T = "rabbit"
 *  
 *  Return 3.
 */
int count(string s, string t) {
  int len_s = s.length();
  int len_t = t.length();

  if(len_s == 0 && len_t == 0) return 0;
  if(len_s == 0) return 0;

  // mem[i][j] = # of distinct subsequences of s[1..i] in t[1..j]
  vector<vector<int> > mem(len_s + 1, vector<int>(len_t + 1, 0));
  
  // "" is a subsequence of ""
  mem[0][0] = 1;
  
  // delete all chars in s results "" which is a subsequence of t = ""
  for (int i = 1; i <= len_s; ++i)
    mem[i][0] = 1;

  // "" is not a subsequence of a non-empty string
  for (int i = 1; i <= len_t; ++i)
    mem[0][i] = 0;

  for (int i = 1; i <= len_s; ++i)
    for (int j = 1; j <= len_t; ++j)
      mem[i][j] = s[i - 1] == t[j - 1] ? mem[i - 1][j] + mem[i - 1][j - 1] : mem[i - 1][j];

  return mem[len_s][len_t];
}

int main() {
  cout << count("a", "b") << endl;
  cout << count("b", "b") << endl;
  cout << count("ccc", "c") << endl;
  cout << count("rabbbit", "rabbit") << endl;
  return 0;
}

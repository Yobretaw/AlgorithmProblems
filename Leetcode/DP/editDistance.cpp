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
 *  Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
 *  
 *  You have the following 3 operations permitted on a word:
 *  
 *  a) Insert a character
 *  b) Delete a character
 *  c) Replace a character
 */
int editDist(string s1, string s2) {
  int len1 = s1.length();
  int len2 = s2.length();

  if(len1 == 0 || len2 == 0)
    return len1 == 0 ? len2 : len1;

  // mem[i][j] = the minimum edit distance between s1[1, i] and s2[1, j]
  vector<vector<int> > mem(len1 + 1, vector<int>(len2 + 1, 0));
  
  for (int i = 1; i <= len1; ++i)
    mem[i][0] = i;

  for (int i = 1; i <= len2; ++i)
    mem[0][i] = i;

  for (int i = 1; i <= len1; ++i)
    for (int j = 1; j <= len2; ++j)
      if(s1[i - 1] == s2[j - 1])
        mem[i][j] = mem[i - 1][j - 1];
      else
        //                      replace               insert          delete
        mem[i][j] = 1 + min(mem[i - 1][j - 1], min(mem[i - 1][j], mem[i][j - 1]));

  return mem[len1][len2];
}

// 滚动数组
int editDist2(strings s1, string s2) {
  int len1 = s1.length();
  int len2 = s2.length();

  if(len1 == 0 || len2 == 0)
    return len1 == 0 ? len2 : len1;

  vector<int> mem(len2 + 1);
  int upper_left = 0;   // extra variable to record mem[i - 1][j - 1]

  for (int i = 0; i <= len2; ++i)
    mem[i] = i;

  for (int i = 1; i <= len1; ++i) {
    upper_left = mem[0];
    mem[0] = i;

    for (int j = 1; j <= len2; ++j) {
      int upper = mem[j];   // mem[i - 1][j]

      if(s1[i - 1] == s2[j - 1])
        mem[j] = upper_left;
      else
        mem[j] = 1 + min(upper_left, min(mem[j], mem[j - 1]));

      upper_left = upper;
    }
  }
  return mem[len2];
}

int main() {
  return 0;
}

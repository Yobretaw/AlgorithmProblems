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
 *  Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
 *  
 *  Below is one possible representation of s1 = "great":
 *  
 *      great
 *     /    \
 *    gr    eat
 *   / \    /  \
 *  g   r  e   at
 *             / \
 *            a   t
 *  To scramble the string, we may choose any non-leaf node and swap its two children.
 *  
 *  For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
 *  
 *      rgeat
 *     /    \
 *    rg    eat
 *   / \    /  \
 *  r   g  e   at
 *             / \
 *            a   t
 *  We say that "rgeat" is a scrambled string of "great".
 *  
 *  Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
 *  
 *      rgtae
 *     /    \
 *    rg    tae
 *   / \    /  \
 *  r   g  ta  e
 *         / \
 *        t   a
 *  We say that "rgtae" is a scrambled string of "great".
 *  
 *  Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
 */
/*
 *  分析：
 *  这个问题是google的面试题。由于一个字符串有很多种二叉表示法，貌似很难判断两个字符串是否可以做这样的变换。
 *  对付复杂问题的方法是从简单的特例来思考，从而找出规律。
 *  先考察简单情况：
 *  字符串长度为1：很明显，两个字符串必须完全相同才可以。
 *  字符串长度为2：当s1="ab", s2只有"ab"或者"ba"才可以。
 *  对于任意长度的字符串，我们可以把字符串s1分为a1,b1两个部分，s2分为a2,b2两个部分，满足（(a1~a2) && (b1~b2)）或者 （(a1~b2) && (b1~a2)）
 */
bool isScramble(string s1, string s2) {
  int len1 = s1.length();
  int len2 = s2.length();

  if(len1 != len2) return false;

  if(s1 == s2) return true;

  if(len1 == 2) {
    return (s1[0] == s2[1]) && (s1[1] == s2[0]);
  }

  // two strings must have same number of each letters
  string tmp1 = s1, tmp2 = s2;
  sort(tmp1.begin(), tmp1.end());
  sort(tmp2.begin(), tmp2.end());
  if(tmp1 != tmp2) return false;

  for (int i = 1; i < len1; ++i) {
    string a1 = s1.substr(0, i);
    string b1 = s1.substr(i, len1 - i);
    string a2 = s2.substr(0, i);
    string b2 = s2.substr(i, len1 - i);
    if(isScramble(a1, a2) && isScramble(b1, b2)) return true;

    a2 = s2.substr(0, len2 - i);
    b2 = s2.substr(len2 - i, i);
    if(isScramble(a1, b2) && isScramble(b1, a2)) return true;
  }
  return false;
}

/*
 *  解法二（动态规划）：
 *  减少重复计算的方法就是动态规划。
 *  
 *  这里我使用了一个三维数组 boolean result[len][len][len],其中第一维为子串的长度，第二维为s1的起始索引，第三维为s2的起始索引。
 *  result[k][i][j] 表示 s1[i...i+k] 是否可以由 s2[j...j+k] 变化得来。
 */
bool isScramble2(string s1, string s2) {
  int len1 = s1.length();
  int len2 = s2.length();

  if(len1 != len2)
    return false;

  if(s1 == s2)
    return true;

  if(len1 == 2)
    return (s1[0] == s2[1]) && (s1[1] == s2[0]);

  vector<vector<vector<int> > > mem(len1, vector<vector<int> >(len1, vector<int>(len1, 0)));

  for (int i = 0; i < len1; ++i)
    for (int j = 0; j < len1; ++j)
      mem[0][i][j] = s1[i] == s2[j];

  for (int k = 2; k <= len1; ++k) {
    for (int i = len1 - k; i >= 0; --i) {
      for(int j = len1 - k; j >= 0; --j) {
        bool r = false;
        for (int m = 1; m < k && !r; ++m) {
          r = (mem[m-1][i][j] && mem[k-m-1][i+m][j+m]) || (mem[m-1][i][j+k-m] && mem[k-m-1][i+m][j]);
        }
        mem[k - 1][i][j] = r;
      }
    }
  }
  return mem[len1 - 1][0][0];
}

int main() {
  cout << isScramble("great", "rgtae") << endl;
  cout << isScramble("great", "rgeat") << endl;

  cout << isScramble2("great", "rgtae") << endl;
  cout << isScramble2("great", "rgeat") << endl;
  return 0;
}

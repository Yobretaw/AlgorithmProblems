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

void combinationHelp(const string& s, unordered_map<char, vector<char> >& m, int idx, vector<char>& path, vector<vector<char> >& result);

/* Given a digit string, return all possible letter combination that the number
 * could represent.
 * 
 * The mapping of digit to letter:
 *    2: a, b, c
 *    3: d, e, f
 *    4: g, h, i
 *    5: j, k, l
 *    6: m, n, o
 *    7: p, q, r
 *    8: s, t, u
 *    9: v, w, x, z
 *
 *    Input:Digit string "23"
 *    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
 */
vector<vector<char> > letterCombination(const string& s) {
  vector<vector<char> > result;

  unordered_map<char, vector<char> > m;

  m['2'] = {'a', 'b', 'c'};
  m['3'] = {'d', 'e', 'f'};
  m['4'] = {'g', 'h', 'i'};
  m['5'] = {'j', 'k', 'l'};
  m['6'] = {'m', 'n', 'o'};
  m['7'] = {'p', 'q', 'r'};
  m['8'] = {'s', 't', 'u'};
  m['9'] = {'v', 'w', 'x', 'z'};

  vector<char> path;
  combinationHelp(s, m, 0, path, result);
  return result;
}

void combinationHelp(const string& s, unordered_map<char, vector<char> >& m, int idx, vector<char>& path, vector<vector<char> >& result) {
  if(idx == s.length()) {
    result.push_back(path);
    return;
  }
  for (int i = 0; i < m[s[idx]].size(); ++i) {
    path.push_back(m[s[idx]][i]);
    combinationHelp(s, m, idx + 1, path, result);
    path.pop_back();
  }
}

int main() {
  string s = "23";
  vector<vector<char> > result = letterCombination(s);
  for (int i = 0; i < result.size(); ++i) {
    for (int j = 0; j < result[i].size(); ++j) {
      cout << result[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}

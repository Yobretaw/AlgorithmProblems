#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include <unordered_set>
using namespace std;

/*
 *  Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
 *  
 *  Return all such possible sentences.
 *  
 *  For example, given
 *  s = "catsanddog",
 *  dict = ["cat", "cats", "and", "sand", "dog"].
 *  
 *  A solution is ["cats and dog", "cat sand dog"].
 */
void gen_path(const string& s, const vector<vector<bool> >& prev, int curr, vector<string>& path, vector<string>& result) {
  if(curr == 0) {
    string tmp;
    for(auto iter = path.crbegin(); iter != path.crend(); ++iter)
      tmp += *iter + " ";

    tmp.erase(tmp.end() - 1);
    result.push_back(tmp);
  }
  for(int i = 0; i < curr; ++i) {
    if(prev[curr][i]) {
      path.push_back(s.substr(i, curr - i));
      gen_path(s, prev, i, path, result);
      path.pop_back();
    }
  }
}

vector<string> wordBreak(string s, unordered_set<string>& dict) {
  int n = s.length();
  vector<bool> mem(n + 1, false);

  vector<vector<bool> > prev(n + 1, vector<bool>(n));
  mem[0] = true;

  for(int i = 1; i <= n; ++i) {
    for(int j = i - 1; j >= 0; --j) {
      if(mem[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
        mem[i] = true;
        prev[i][j] = true;
      }
    }
  }
  vector<string> result;
  vector<string> path;
  gen_path(s, prev, n, path, result);
  return result;
}

int main() {
 //string s = "catsanddog";
 //unordered_set<string> dict = { "cat", "cats", "and", "sand", "dog" };
 string s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab";
 unordered_set<string> dict = {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"};
 vector<string> result = wordBreak(s, dict);
 for (auto s : result) {
   cout << s << endl;
 }
}

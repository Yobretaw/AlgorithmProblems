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

/******************************************************************************************
 * Given a string, partition s such that every substring of the partition is a palindrome.
 * Return all possible palindrome partition of s.
 * 
 * For example, given s = "aab", return
 * [
 *   ["aa", "b"],
 *   ["a", "a", "b"]
 * ]
 */
vector<vector<int> > calc(const string& s) {
  vector<vector<int> > p(s.length(), vector<int>(s.length(), 0));
  
  int len = s.length();
  for(int i = len - 1; i >= 0; --i)
    for (int j = i; j < len; ++j)
      if(s[i] == s[j] && (j - i < 2 || p[i + 1][j - 1]))
        p[i][j] = 1;

  return p;
}

void partition_help(const string& s, const vector<vector<int> >& p, int idx, vector<string>& path, vector<vector<string> >& result) {
  int len = s.length();
  if(idx == len) {
    result.push_back(path);
    return;
  }

  for (int i = idx; i < len; ++i) {
    if(p[idx][i]) {
      path.push_back(s.substr(idx, i - idx + 1));
      partition_help(s, p, i + 1, path, result);
      path.pop_back();
    }
  }
}

vector<vector<string> > partition(const string& s) {
  vector<vector<string> > result;
  vector<vector<int> > p = calc(s);
  vector<string> path;
  partition_help(s, p, 0, path, result);
  return result;
}

// this method is wayyyyyyyy to slow :(
vector<vector<string> > partition2(const string& s) {
  int len = s.length();
  vector<vector<int> > p = calc(s);
  vector<vector<vector<string> >> sub_pal(len);
  for (int i = len - 1; i >= 0; --i) {
    for (int j = i; j < len; ++j) {
      if(p[i][j]) {
        const string pal = s.substr(i, j - i + 1);
        if(j + 1 < len) {
          for(auto v : sub_pal[j + 1]) {
            v.insert(v.begin(), pal);
            sub_pal[i].push_back(v);
          }
        } else {
          vector<string> m(1, pal);
          sub_pal[i].push_back(m);
        }
      }
    }
  }
  return sub_pal[0];
}

int main() {
  vector<vector<string> > result = partition2("aaaaaaaaaaaaaaaaaaaaa");
  //vector<vector<string> > result = partition2("aaaabaabaabaaaabaabaabaaabaabaaba");
  //vector<vector<string> > result = partition2("seeslaveidemonstrateyetartsnomedievalsees");
  //for(auto v : result) {
  //  for(auto s : v) {
  //    cout << s << " ";
  //  }
  //  cout << endl;
  //}
  return 0;
}


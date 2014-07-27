#include "iostream"
#include "string"
#include "map"
#include "vector"
using namespace std;

// Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
// For example, given
// s = "leetcode",
// dict = ["leet", "code"].
// Return true because "leetcode" can be segmented as "leet code".

bool wordBreak(string s, vector<string>& dict) {
  bool t[s.length() + 1];
  memset(t, 0, sizeof(t));

  t[0] = 1;

  for(int i = 0; i < (int)s.length(); i++) {
    // should start from match position
    if(!t[i])
      continue;

    for(int j = 0; j < (int)dict.size(); j++) {
      string word = dict[j];

      int end = i + word.length();
      if(end > (int)s.length() || t[end])
        continue;

      if(s.substr(i, end - i) == word) {
        t[end] = true;
      }
    }
  }

  return t[s.length()];
}

int main()
{
  vector<string> dict;

  dict.push_back("hello");
  dict.push_back("world");
  dict.push_back("foo");
  dict.push_back("bar");
  int result = wordBreak("barfooworldhello", dict);
  cout << result << endl;

  //dict.push_back("programcree");
  //dict.push_back("program");
  //dict.push_back("creek");
  //cout << wordBreak("programcreek", dict) << endl;
  return 0;
}

#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

// Given a string without spaces, if you can insert spaces into this string such that each word separated by the space in the resulting string exists in the dictionary, then this string is a sentence. You are given a function word(w), which takes a string w as input and tells whether this word is in the dictionary in O(1). Give a dynamic programming algorithm to determine whether the input string s is a sentence.
bool formSentenceHelp(const string& s, const unordered_map<string, bool>& dict, int start, vector<vector<int> >& seen) {
  static int count = 0;
  if(start >= s.length()) {
    return true;
  }

  int slen = s.length();
  for (int i = start + 1; i <= slen; i++) {
    string curr = s.substr(start, i - start);
    count++;
    cout << count << endl;
    //if(!seen[i][slen-1] && dict.count(curr) == 1 && formSentenceHelp(s, dict, i, seen)) {
    if(dict.count(curr) == 1 && formSentenceHelp(s, dict, i, seen)) {
      return true;
    }

    seen[i][slen-1] = 1;
  }

  return false;
}

bool formSentence(const string& s, const unordered_map<string, bool>& dict) {
  vector<vector<int> > seen(s.length() + 1, vector<int>(s.length() + 1));
  cout << s.length() << endl;
  return formSentenceHelp(s, dict, 0, seen);
}

int main()
{
  unordered_map<string, bool> dict;
  dict["I"] = 1;
  dict["am"] = 1;
  dict["ama"] = 1;
  dict["king"] = 1;

  cout << formSentence("IamkingIamkingamaIamamamkingI", dict);
  return 0;
}

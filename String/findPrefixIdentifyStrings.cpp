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

// Given a list of string, return the list of prefix that can uniquely define each string.
vector<string> findPrefix(vector<string>& list) {
  int len = list.size();

  if(len == 0) return vector<string>();
  if(len == 1) return vector<string>{ string(list[0], 0, 1) };

  vector<string> result;
  //vector<int> indexes(len, 0);
  sort(list.begin(), list.end());
  int curr = 0, next = 0;

  for(int i = 0; i < len - 1; ++i) {
    // found two same strings, return empty prefix list
    if(list[i] == list[i + 1]) return vector<string>();

    while(curr < list[i].length() &&
          next < list[i + 1].length() &&
          list[i][curr] == list[i + 1][next]) {
      curr++;
      next++;
    }
    if(curr >= list[i].length())
      curr = list[i].length() - 1;

    result.push_back(list[i].substr(0, curr + 1));
    curr = next;
  }
  
  // insert last string
  if(curr >= list[len - 1].length())
    curr = list[len - 1].length() - 1;

  result.push_back(list[len - 1].substr(0, curr + 1));
  return result;
}

int main() {
  vector<string> v = {
    "abcde",
    "abe",
    "ab",
    "abcdef",
    "abcdeh"
  };
  vector<string> result = findPrefix(v);
  for(auto s : result) cout << s << endl;
  return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

/* Given an array of strings, return all strings that have anagrams
 *
 * Note: ALl input will be in lower-case
 */
vector<string> findAnagrams(vector<string> input) {
  unordered_map<string, vector<string> > map;
  
  for (int i = 0; i < input.size(); ++i) {
    string curr = input[i];
    sort(curr.begin(), curr.end());

    if(map.count(curr) == 0) {
      map[curr] = vector<string>();
    }
    map[curr].push_back(input[i]);
  }

  vector<string> result;
  for (auto it = map.begin(); it != map.end(); it++) {
    // no anagrams
    if(it->second.size() == 1)
      continue;

    result.insert(result.end(), it->second.begin(), it->second.end());
  }

  return result;
}

int main() {
  vector<string> input = { "abc", "cba", "ca" };
  vector<string> result = findAnagrams(input);
  for (int i = 0; i < result.size(); ++i) {
    cout << result[i] << endl;
  }
  return 0;
}

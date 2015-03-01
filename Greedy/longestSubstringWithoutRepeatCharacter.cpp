#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <climits>
using namespace std;

/* Given a string, find the length of the longest substring without
 * repeating characters. For example, the longest substring without
 * without repeating letters for ”abcabcbb” is ”abc”, which the length
 * is 3. For "bbbbb" the longest substring is ”b”, with the length of 1.
 */
string find(const string& s) {
  int start = 0;
  int max_len = 0;
  int max_start = 0;
  vector<int> pos(256, -1);

  for (int i = 0; i < s.length(); i++) {
    if(pos[s[i]] >= start)
      start = pos[s[i]] + 1;

    pos[s[i]] = i;

    if(i - start >= max_len) {
      max_len = i - start + 1;
      max_start = start;
    }
  }

  return s.substr(max_start, max_len);
}


int main() {
  //cout << find(" ") << endl;
  cout << find("hchzvfrkmlnozjk") << endl;
  //cout << find("geekforgeeks") << endl;
  //cout << find("manisleasthimselfwhentalksinhisownperon") << endl;
  cout << find("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco") << endl;
  return 0;
}

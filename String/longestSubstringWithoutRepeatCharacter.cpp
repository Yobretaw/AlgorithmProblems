#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <climits>
using namespace std;

string find(const string& s) {
  int count[256];
  for (int i = 0; i < 256; i++) {
    count[i] = -1;
  }

  int start = 0;
  int max_len = 0;
  int max_start = 0;

  for (int i = 0; i < s.length(); i++) {
    if(count[s[i]] < 0) {
      count[s[i]] = i;

      if(i - start > max_len) {
        max_len = i - start;
        max_start = start;
      }
    } else {
      if(count[s[i]] >= start) {
        start = count[s[i]] + 1;
      } else if(i - start > max_len){
        max_len = i - start;
        max_start = start;
      }

      count[s[i]] = i;
    }
  }
  return s.substr(max_start, max_len + 1);
}

int main() {
  cout << find("geekforgeeks") << endl;
  cout << find("manisleasthimselfwhentalksinhisownperon") << endl;
  return 0;
}

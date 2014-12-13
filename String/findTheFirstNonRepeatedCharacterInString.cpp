#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

char find(const string& s) {
  unordered_map<char, int> m;
  int count[256] = {0};
  for (int i = 0; i < (int)s.length(); ++i) {
    if(count[s[i]] == 1)
      count[s[i]] = 0;
    else
      count[s[i]] = 1;
  }

  for (int i = 0; i < (int)s.length(); ++i) {
    if(count[s[i]] == 1)
      return s[i];
  }

  return '0';
}

int main() {
  cout << find("geekforgeeks") << endl;
  return 0;
}

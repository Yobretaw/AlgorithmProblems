#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

string charToNumber(const string& str) {
  string ret = "";

  for (int i = 0; i < str.length(); i++) {
    char c = str[i];
    if(c < 'a')
      c = 'a' + c - 'A';

    if('a' <= c && c <= 'o') {
      ret += '2' + (c - 'a') / 3;
    } else if('p' <= c && c <= 's') {
      ret += '7';
    } else if('t' <= c && c <= 'v')  {
      ret += 8;
    } else {
      ret += '9';
    }
  }
  return ret;
}

int main() {
  cout << charToNumber("Amazon") << endl;
  return 0;
}

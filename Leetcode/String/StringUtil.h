#include <iostream>
#include <vector>
#include <string>
using namespace std;

string reverseString(string s) {
  int start = 0, end = s.length() - 1;
  while(start < end) {
    swap(s[start++], s[end--]);
  }

  return s;
}

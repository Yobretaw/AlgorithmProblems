#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

char toLowercase(char c) {
  if('A' <= c && c <= 'Z') return 'a' + c - 'A';
  else return c;
}

bool isInRange(char c) {
  return (c >= 'a' && c <= 'z')
      || (c >= 'A' && c <= 'Z')
      || ('0' <= c && c <= '9');
}

bool isPalindrome(const string& s) {
  int len = s.length();
  if(len == 0 || len == 1)
    return true;

  int start = 0, end = len - 1;
  while(start < len) {
    while(start < end && !isInRange(s[start])) start++;
    while(start < end && !isInRange(s[end])) end--;

    if(start >= end) break;
    if(toLowercase(s[start++]) != toLowercase(s[end++]))
      return false;
  }
  return true;
}

int main() {
  string s = "A man, a plan, a canal: Panama";
  cout << isPalindrome(s) << endl;
  return 0;
}

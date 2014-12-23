#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

void reverseStr(string& s) {
  int len = s.length();
  for(int i = 0; i < len / 2; i++)
    swap(s[i], s[len - i - 1]);
}

string bigAdd(string s1, string s2) {
  int len1 = s1.length();
  int len2 = s2.length();

  reverseStr(s1);
  reverseStr(s2);
  string result = "";

  int carry = 0, curr = 0;
  for(int i = 0; i < max(len1, len2); ++i) {
    if(i >= len1)
      curr = s2[i] - '0';
    else if(i >= len2)
      curr = s1[i] - '0';
    else
      curr = (s1[i] - '0') + (s2[i] - '0');

    curr += carry;
    carry = curr / 10;
    curr %= 10;

    result += '0' + curr;
  }
  if(carry != 0)
    result += '1';

  reverseStr(result);
  return result;
}

int main() {
  string s1 = "1123128327980370219";
  string s2 = "6034820348092384023840324";

  string result = bigAdd(s1, s2);
  cout << result << endl;
  return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include "StringUtil.h"
#include <unordered_map>
using namespace std;

/* Given two binary strings, return their sum(also a binary string)
 *
 * For example, a = "11", b = "1", return "100"
 */
string addBinary(string a, string b) {
  int alen = a.length();
  int blen = b.length();
  string ret = "";

  int ai = alen - 1, bi = blen - 1;
  int carry = 0, curr = 0, base = 2;
  while(ai >= 0 || bi >= 0) {
    curr = carry;
    if(ai >= 0) curr += a[ai--] - '0';
    if(bi >= 0) curr += b[bi--] - '0';

    carry = curr / base;
    curr %= base;

    ret += '0' + curr;
  }

  // possibly extra bit
  if(carry > 0)
    ret += '0' + carry;

  return reverseString(ret);
}

int main() {
  string a = "11";
  string b = "1";

  cout << addBinary(a, b) << endl;
  return 0;
}

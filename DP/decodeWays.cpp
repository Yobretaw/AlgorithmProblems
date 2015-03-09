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

/*
 *  A message containing letters from A-Z is being encoded to numbers using the following mapping:
 *  
 *    'A' -> 1
 *    'B' -> 2
 *    ...
 *    'Z' -> 26
 *
 *  Given an encoded message containing digits, determine the total number of ways to decode it.
 *  
 *  For example,
 *  Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
 *  
 *  The number of ways decoding "12" is 2.
 */
int decodeWays(string msg) {
  int n = msg.length();

  if(n == 0 || msg[0] == '0') return 0;
  int prev = 0, curr = 1;
  for (int i = 1; i <= n; ++i) {
    if(msg[i - 1] == '0')
      curr = 0;

    if(i < 2 || !(msg[i - 2] == '1' || (msg[i - 2] == '2' && msg[i - 1] <= '6')))
      prev = 0;

    int tmp = curr;
    curr += prev;
    prev = tmp;
  }
  return curr;
}

int main() {
  //cout << (decodeWays("1212") == 5) << endl;
  //cout << decodeWays("10") << endl;
  //cout << decodeWays("010") << endl;
  //cout << decodeWays("100") << endl;
  //cout << decodeWays("1010") << endl;
  //cout << decodeWays("27") << endl;
  //cout << decodeWays("2727") << endl;
  //cout << decodeWays("99") << endl;
  //cout << decodeWays("110") << endl;
  //cout << decodeWays("31") << endl;
  //cout << (decodeWays("611") == 2) << endl;
  //cout << (decodeWays("26") == 2) << endl;
  cout << decodeWays("111111111111") << endl;
  cout << decodeWays("121212121212") << endl;
  return 0;
}

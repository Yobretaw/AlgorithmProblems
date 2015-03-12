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

bool isNumber(const char& c);
bool isDot(const char& c);
bool isExpSign(const char& c);
bool isPosNegSign(const char& c);
/*
 *  Validate if a given string is numeric.
 *  
 *  Some examples:
 *  "0" => true
 *  " 0.1 " => true
 *  "abc" => false
 *  "1 a" => false
 *  "2e10" => true
 *  Note: It is intended for the problem statement to be ambiguous. You should gather
 *  all requirements up front before implementing one.
 *  
 *  Update (2015-02-10):
 *  The signature of the C++ function had been updated. If you still see your function
 *  signature accepts a const char * argument, please click the reload button  to reset your code definition.
 */
bool isNumber(const string& s) {
  int len = s.length();

  if(len == 0) return false;
  if(len == 1) return isNumber(s[0]);

  int idx = 0;
  while(idx < len && s[idx] == ' ') idx++;
  while(len - 1 >= 0 && s[len - 1] == ' ') len--;
  if(len - 1 < idx) return false;

  bool dot = false;
  bool negPosSign = false;
  bool expSign = false;
  bool dotAfterExpSign = false;
  bool digit = false;
  while(idx < len - 1) {
    char curr = s[idx];
    char next = s[idx + 1];

    if(curr == ' ') return false;

    if(!isDot(curr) &&
        !isExpSign(curr) &&
        !isPosNegSign(curr) &&
        !isNumber(curr))
      return false;

    if(isNumber(curr)) {
      digit = true;

      if(isPosNegSign(next))
        return false;

    } else if(curr == '.') {
      if(dot || isPosNegSign(next) || expSign)
        return false;

      dot = true;

    } else if(isExpSign(curr)) {
      if(expSign || !digit)
        return false;

      expSign = true;
      digit = false;
      negPosSign = false;

    } else if(isPosNegSign(curr)) {
      if(dot && !expSign)
        return false;
      else if(!negPosSign)
        negPosSign = true;
      else
        return false;

      if(!isNumber(next) && (expSign && isDot(next)))
        return false;
    }
    idx++;
  }
  return isNumber(s[idx]) || (!expSign && digit && s[idx] == '.' && !dot);
}

bool isDot(const char& c) { return c == '.'; }
bool isExpSign(const char& c) { return c == 'e'; }
bool isPosNegSign(const char& c) { return c == '+' || c == '-'; }
bool isNumber(const char& c) { return '0' <= c && c <= '9'; }
bool isWhitespace(const char& c) { return c == ' '; }

bool isNumber2(const string& s) {
  int i = 0;

  // skip the whilespaces
  while(isWhitespace(s[i])) i++;

  // check the significand
  if(isPosNegSign(s[i])) i++; // skip the sign if exist

  int digitCount = 0, dotCount = 0;
  while(isNumber(s[i]) || isDot(s[i])) {
    isDot(s[i]) ? dotCount++ : digitCount++;       
    i++;
  }

  if(dotCount > 1 || digitCount < 1) // no more than one point, at least one digit
    return false;

  // check the exponent if exist
  if(isExpSign(s[i])) {
    i++;

    if(isPosNegSign(s[i])) i++; // skip the sign

    bool hasDigit = false;
    while(isNumber(s[i])) {
      i++;
      hasDigit = true;
    }

    if(!hasDigit)
      return false;
  }

  // skip the trailing whitespaces
  while(isWhitespace(s[i])) i++;

  return i == s.length();  // must reach the ending 0 of the string
}

int main() {
  cout << (isNumber2("0") == 1) << endl;
  cout << (isNumber2(" 0") == 1) << endl;
  cout << (isNumber2("0.1") == 1) << endl;
  cout << (isNumber2(" 0.1") == 1) << endl;
  cout << (isNumber2("+.8") == 1) << endl;
  cout << (isNumber2("3.") == 1) << endl;
  cout << (isNumber2("2e10") == 1) << endl;
  cout << (isNumber2("2e-10") == 1) << endl;
  cout << (isNumber2("-2e-10") == 1) << endl;
  cout << (isNumber2("-2e10") == 1) << endl;
  cout << (isNumber2("-2.3e10") == 1) << endl;
  cout << (isNumber2("46.e3") == 1) << endl;
  cout << (isNumber2("32.e-80123") == 1) << endl;
  cout << "--------------------------------" << endl;
  cout << (isNumber2(" 4e3.") == 0) << endl;
  cout << (isNumber2("6e6.5") == 0) << endl;
  cout << (isNumber2(".+8") == 0) << endl;
  cout << (isNumber2("1e.") == 0) << endl;
  cout << (isNumber2(" .") == 0) << endl;
  cout << (isNumber2("e") == 0) << endl;
  cout << (isNumber2("e9") == 0) << endl;
  cout << (isNumber2("abc") == 0) << endl;
  cout << (isNumber2("1 a") == 0) << endl;
  cout << (isNumber2("-2.3e-0.1") == 0) << endl;
  cout << (isNumber2("-2.3e1.0") == 0) << endl;
  return 0;
}

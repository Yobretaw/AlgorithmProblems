#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

unordered_map<char*, unordered_map<char*, bool> > seen;
bool matchFirst(const char* s, const char *p);

/* Implement regular expression matching with support for '.' and '*'
 * '.' matches any single character. '*' matches zero or more of the
 * preceding element.
 *
 * The matching should cover the entire input string(not partial)
 *
 * The function prototype should be:
 *    - bool isMatch(const char *s, const char *p)
 *    
 * Some examples:
 *
 *    isMatch("aa","a") → false
 *    isMatch("aa","aa") → true
 *    isMatch("aaa","aa") → false
 *    isMatch("aa", "a*") → true
 *    isMatch("aa", ".*") → true
 *    isMatch("ab", ".*") → true
 *    isMatch("aab", "c*a*b") → true
 */
bool isMatch(const char *s, const char *p) {
  if(!*p) return !*s;
  
  if(p[1] != '*' && p[1] != '+') {
    if(!matchFirst(s, p)) return false;
    return isMatch(s + 1, p + 1);
  } else {
    if(p[1] == '*' && isMatch(s, p + 2)) return true;
    if(p[1] == '+' && isMatch(s + 1, p + 2)) return true;

    while(matchFirst(s, p))
      if(isMatch(++s, p + 2)) return true;
    return false;
  }
}

bool matchFirst(const char* s, const char *p) {
  return (*p == *s) || (*p == '.' && *s);
}

int main() {
  cout << isMatch((char*)"aab",   (char*)"c*a*b") << endl;
  cout << isMatch((char*)"aaa",   (char*)"a*a") << endl;
  cout << isMatch((char*)"abcd",  (char*)"abcd*") << endl;
  cout << isMatch((char*)"abb",   (char*)"ab*") << endl;
  cout << isMatch((char*)"a",   (char*)"ab*") << endl;
  cout << isMatch((char*)"bbbba", (char*)".*a*a") << endl;
  cout << isMatch((char*)"aa", (char*)"a") << endl;
  cout << isMatch((char*)"aaa", (char*)"ab*a") << endl;
  cout << isMatch((char*)"aaaaaaaaaaaaab", (char*)"a*a*a*a*a*a*a*a*a*a*c") << endl;

  cout << isMatch((char*)"aaa", (char*)"a+b*a") << endl;
  cout << isMatch((char*)"aaa", (char*)"a+") << endl;
  cout << isMatch((char*)"a", (char*)"a+") << endl;
  cout << isMatch((char*)"a", (char*)"a+") << endl;
  cout << isMatch((char*)"abbbccd",  (char*)"ab+.*cd*") << endl;
  cout << isMatch((char*)"abbbccd",  (char*)"a+.+.*c+d+") << endl;

  return 0;
}

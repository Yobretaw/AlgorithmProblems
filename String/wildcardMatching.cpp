#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

unordered_map<char*, unordered_map<char*, bool> > seen;
/* Implement wildcard pattern matching with support for '?' and '*'.
 * 
 * '?' matches any single character. '*' matches any sequence of character
 * (including the empty sequence).
 *
 * The matching should cover the entire input string.
 */
bool isMatch(const char *s, const char *p) {
  if(!*p) return !*s;

  char *astroid = NULL;
  char *s1 = (char*)s;

  while(*s) {
    // match single character
    if(*p == '?' || *p == *s) {
      s++;
      p++;
      continue;
    }

    // meet an astroid, save its location and proceeds
    if(*p == '*') {
      astroid = (char*)p++;
      s1 = (char*)s;
      continue;
    }

    if(astroid) {
      p = astroid + 1;
      s = ++s1;
      continue;
    }

    return false;
  }

  while(*p == '*') p++;
  return !*p;
}

int main() {
  cout << isMatch((char*)"aa", (char*)"a") << endl;
  cout << isMatch((char*)"aa", (char*)"aa") << endl;
  cout << isMatch((char*)"aaa", (char*)"aa") << endl;
  cout << isMatch((char*)"aa", (char*)"*") << endl;
  cout << isMatch((char*)"aa", (char*)"?*") << endl;
  cout << isMatch((char*)"aab", (char*)"c*a*b") << endl;
  cout << isMatch((char*)"babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", (char*)"***bba**a*bbba**aab**b") << endl;
  cout << isMatch((char*)"aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", (char*)"a*******b") << endl;
  cout << isMatch((char*)"ababaabaabbbbbabbbaaababbaabbbbbaaabaabababaaaabbabbbbabbaaaaaaaaabaababbaabaaababaababaabbabbbbbabababbabaabbbaababbbababaaabbbbbbbbbabaababaaabababbbbabbaabaaabbbababbbbbbbbabaaaabbabbbbabbaaabbbbababab", (char*)"ab**bbb*a*ab*bb*aa*a***ab*b**b***bba****b*aaabaa**bb*ab*a***abb****bb*a**b*****a*abaa**a****aab**aa**bbb") << endl;
  cout << isMatch((char*)"bbbbbabababbbabbbbaaabbbbabbaabbaabbaabaaabaaababbabababaaaaabaabbbabaaabbababbbaababbbbbbaaaaabbabaababbabbbaababbabababbabbbbababbabbbaaabaabbaabbbabaaaabbbaabbbbaaaaaaabbbabbbaabbbbbbbaababaabaabbb", (char*)"***ba**bbaaa*b***bba*abaa*aaa****b***baababab***ab**ba*b**b**bba*a**b******a******aa**bbb*a**b**b*a*b") << endl;
  cout << isMatch((char*)"abcdec", (char*)"ab*c") << endl;
  return 0;
}

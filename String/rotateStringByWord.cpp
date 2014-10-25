#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int nextWhitespace(string& s, int start) {
  while(start < s.length() && !isspace(s[start]))
    start++;

  return start;
}

// "foo bar baz lol" -> "lol baz bar foo"
// algorithm:
//
//  first we reverse each word in the string:
//     --> "oof rab zab lol"
//
//  then we rotate the whole string
//    --> "lol baz bar foo"
//
//  done.
void reverse(string& s) {
  int len = s.length();

  if(len == 0 || len == 1)
    return;

  int idx = 0;
  while(idx < len) {
    while(isspace(s[idx])) {
      idx++;
    }

    int nextPos = nextWhitespace(s, idx);
    int beforeNextPos = nextPos - 1;

    while (idx < beforeNextPos) {
      swap(s[idx++], s[beforeNextPos--]);
    }
    
    idx = nextPos + 1;
  }

  idx = 0;
  len--;
  while (idx < len) {
    swap(s[idx++], s[len--]);
  }
}

int main()
{
  //string s = "foo bar baz lol";
  string s = "I am a student";
  reverse(s);
  cout << s << endl;
  return 0;
}

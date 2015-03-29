#include "iostream"
using namespace std;

// Given a string s, remove 'ac' and 'b' from it
void remove(string& s) {
  if(s.length() == 0)
    return;

  int curr = 0;
  int next = 0;

  while(s[next] != '\0') {
    char c = s[next];
    char nextChar = s[next+1];

    if(c == 'b') {
      next++;
      continue;
    }

    if(nextChar == '\0') {
      s[curr++] = c;
      break;
    }

    if(c == 'a' && nextChar == 'c')
      next += 2;
    else
      s[curr++] = s[next++];
  }

  s[curr] = '\0';
  return;
}

int main()
{
  string s = "abc";
  //string s = "bacc";
  remove(s);
  cout << s << endl;
  return 0;
}

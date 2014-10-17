#include "iostream"
#include "string"
using namespace std;

void printString(string s, int start = 0);

void printString(string s, int start) {
  if(start == (int)s.length() - 1) {
    cout << s << endl;
    return;
  }

  for(int i = start; i < (int)s.length(); i++) {
    // avoid duplicates
    if(i != start && s[i] == s[start])
      continue;
    
    swap(s[start], s[i]);
    printString(s, start + 1);
    swap(s[start], s[i]);
  }
}

int main()
{
  printString("abcdefg");
  return 0;
}

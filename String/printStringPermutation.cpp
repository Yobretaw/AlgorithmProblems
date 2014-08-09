#include "iostream"
#include "string"
using namespace std;

void printString(string s, int start) {
  if(start == (int)s.length() - 1) {
    cout << s << endl;
    return;
  }

  for(int i = start; i < (int)s.length(); i++) {
    // adding this if statement to avoid duplicates
    if(i != start && s[i] == s[start])
      continue;
    
    char temp = s[start];
    s[start] = s[i];
    s[i] = temp;

    printString(s, start + 1);

    temp = s[start];
    s[start] = s[i];
    s[i] = temp;
  }
}

int main()
{
  printString("abcd", 0);
  return 0;
}

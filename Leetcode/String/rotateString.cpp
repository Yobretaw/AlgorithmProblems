#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

// rotate string in place:
// if input "abcdef" and rotate the first two letters
// should output "cdefab"

void reverseString(string& s, int start, int end) {
  while (start < end) {
    swap(s[start++], s[end--]);
  }
}

void rotate(string& s, int m) {
  int n = s.length();

  m %= n;
  reverseString(s, 0, m-1);
  reverseString(s, m, n-1);
  reverseString(s, 0, n-1);
}

int main()
{
  string s = "abcdef";
  rotate(s, 2);
  cout << s << endl;
  return 0;
}

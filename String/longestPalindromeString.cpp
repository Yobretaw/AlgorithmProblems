#include "iostream"
#include "string"
#include "stdlib.h"
using namespace std;

string preProcess(string s) {
  string ret = "#";
  for(int i = 0; i < (int)s.length(); i++) {
    ret += s[i];
    ret += "#";
  }

  return ret;
}

string longestPalSubstring(string s) {
  if(s.length() == 0)
    return "";

  s = preProcess(s);
  
  int currCenter = 0;
  int maxCenter = 0;
  int maxRadius = 0;
  int rightEnd = 0;

  int p[s.length()];
  memset(p, 0, sizeof(p));

  for(int i = 0; i < (int)s.length(); i++) {
    p[i] = (rightEnd > i)
      ? min(p[2 * currCenter - i], rightEnd - i)
      : 1;

    while(s[i + p[i]] == s[i - p[i]])
      p[i]++;

    if(i + p[i] > rightEnd) {
      rightEnd = i + p[i];
      currCenter = i;
    }

    if(p[i] > maxRadius) {
      maxCenter = i;
      maxRadius = p[i];
    }
  }

  if(maxRadius <= 2)
    return "";

  string ret = "";
  for(int i = maxCenter - maxRadius + 2; i <= maxCenter + maxRadius - 2; i+=2)
    ret += s[i];

  return ret;
}

int main()
{
  string s = "HHHeHHHelleoWorld";
  cout << longestPalSubstring(s) << endl;
  return 0;
}

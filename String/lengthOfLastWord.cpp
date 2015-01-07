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

int lengthOfLastWord(const char *s) {
  if(!*s) return 0;
  
  int len = 0;
  while(*s) {
    while(*s && *s == ' ') s++;

    if(!*s) return len;

    len = 0;
    while(*s && *s != ' ') {
      len++;
      s++;
    }
  }

  return len;
}

int main() {
  char *s = (char*)"Hello, world";
  cout << lengthOfLastWord(s) << endl;
  return 0;
}

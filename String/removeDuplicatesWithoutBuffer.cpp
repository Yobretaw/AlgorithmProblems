#include "iostream"
#include "string"
using namespace std;

void remove(string& s) {
  int len = s.length();

  if(len < 2)
    return;

  int tail = 1;
  for(int i = 1; i < len; i++) {
    int j;
    for(j = 0; j < tail; j++) {
      if(s[i] == s[j]) {
        break;
      }
    }

    if(j == tail) {
      s[tail] = s[i];
      tail++;
    }
  }

  s = s.substr(0, tail);
}

int main()
{
  string s = "abebabcxbabebebabbbcabbebebabbs";
  remove(s);
  cout << s << endl;
  return 0;
}



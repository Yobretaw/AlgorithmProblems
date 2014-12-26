#include "iostream"
#include "string"
using namespace std;

void remove(string& s) {
  int tail = 0;

  for (int i = 0; i < (int)s.length(); i++) {
    int j;
    for(j = i+1; j < (int)s.length(); j++) {
      if(s[i] == s[j])
        break;
    }

    if(j == (int)s.length())
      s[tail++] = s[i];

  }
  
  s.resize(tail);
}



int main()
{
  string s = "abebabcxbabebebabbbcabbebebabbs";
  remove(s);
  cout << s << endl;
  return 0;
}



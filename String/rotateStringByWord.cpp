#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

void reverseWord(string& s, int i, int j) {
  while(i < j) {
    swap(s[i++], s[j--]);
  }
}

/*
 *  transfrom "foo bar baz lol" into "lol baz bar foo"
 *  
 *  Algorithm:
 *
 *  first we reverse each word in the string:
 *     --> "oof rab zab lol"
 *
 *  then we rotate the whole string
 *    --> "lol baz bar foo"
 *
 *  Note: 
 *  1. The reversed string should nto contain
 *     leading or trailing spaces
 *  2. Reduct mutiple spaces between words into
 *     a single space
*/     
void reverse(string& s) {
  int len = s.length();

  if(len == 0)
    return;

  int i = 0, j = 0, l = 0;
  bool hasWord = false;
  while(true) {
    while(i < len && s[i] == ' ')
      i++;

    if(i == len) break;
    if(hasWord)
      s[j++] = ' ';

    l = j;
    
    while(i < len && s[i] != ' ')
      s[j++] = s[i++];
    
    reverseWord(s, l, j - 1);
    hasWord = true;
  }

  s.resize(j);
  reverseWord(s, 0, j - 1);
}


int main()
{
  //string s = "foo bar baz lol";
  string s = "I    am a student";
  reverse(s);
  cout << s << endl;
  return 0;
}

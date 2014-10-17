#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

void printStringSubset(string s, int index = 0, string curr = "");

void printStringSubset(string s, int index, string curr) {
  if(s.length() == 0) 
    return;

  unordered_map<char, int> seen;
  for(int i = index; i < s.length(); i++) {
    if(seen[s[i]])
      continue;

    curr += s[i];
    seen[s[i]] = 1;
    
    /**
     if we only want to print subset with certain length, then use this block
     we print all string of length 3, and continue if curr has length at least
     3
     
     if(curr.length() == 3)
       cout << curr << endl;
     else if(curr.length() > 2)
       continue;

     */
    cout << curr << endl;

    printStringSubset(s, i + 1, curr);
    curr.erase(curr.length() - 1);
  }
}


int main(){
  string a = "abcdefg";
  printStringSubset(a);
  return 0;
}

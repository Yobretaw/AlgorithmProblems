#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

void printStringSubset(string s, int startIdx = 0, string curr = "");
void printIntegerSubset(int n, vector<int>& curr, int startIdx);

void printStringSubset(string s, int startIdx, string curr) {
  if(s.length() == 0) 
    return;

  int seen[255] = {0};
  for(int i = startIdx; i < s.length(); i++) {
    if(seen[s[i]] == 1)
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

// print all subset of integers that are less than n
void printIntegerSubset(int n, vector<int>& curr, int startIdx) {
  for(int i = startIdx; i <= n; i++) {
    curr.push_back(i);

    for(int i = 0; i < curr.size(); i++) {
      cout << curr[i];
      if(i != curr.size() - 1) {
        cout << " ";
      }
    }
    cout << endl;

    printIntegerSubset(n, curr, i + 1);
    curr.pop_back();
  }
}


int main(){
  string a = "abcde";
  //printStringSubset(a);
  int input = 15;
  vector<int> curr;
  printIntegerSubset(input, curr, 0);
  return 0;
}

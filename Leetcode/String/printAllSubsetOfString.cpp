#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

void kSubstring(string& str, string &cstr, int s, int k, unordered_map<string, int>& seen);
void printSubsetOfStringHelp(string& str, string& cstr, int s, unordered_map<string, int>& seen);


/* Print all subset of the given string */
void printSubsetOfString(string s) {
  unordered_map<string, int> seen;
  string cstr = "";
  printSubsetOfStringHelp(s, cstr, 0, seen);
}

void printSubsetOfStringHelp(string& str, string& cstr, int s, unordered_map<string, int>& seen) {
  if(cstr.length() <= str.length() && seen[cstr] != 1) {
    cout << cstr << endl;
    seen[cstr] = 1;
  }

  if(s >= str.length()) {
    return;
  }

  int newStart = s + 1;

  /* Elements chosen to be part of the output */
  cstr += str[s];
  printSubsetOfStringHelp(str, cstr, newStart, seen);

  /* Element chosen not to be part of the subset */
  cstr.erase(cstr.length() - 1);
  printSubsetOfStringHelp(str, cstr, newStart, seen);
}

// str: Original string, assumed to be sorted before passing to this function. 
// cstr: Intially empty string where the subset is built.
// s: Index of first element not yet considered for building the set. Initially zero.
// k: Target subset size, assumed to be checked < size of original string.
void kSubstring(string& str, string &cstr, int s, int k, unordered_map<string, int>& seen) {
  if(cstr.length() == k) {
    if(seen[cstr] != 1) {
      cout << cstr << endl;
      seen[cstr] = 1;
    }

    return;
  }

  if(s >= str.length()) {
    return;
  }

  /* Skip all duplicates */
  int newStart = s + 1;
  while(str[newStart] && str[s] == str[newStart]) {
    newStart++;
  }

  /* Elements chosen to be part of the output */
  cstr += str[s];
  kSubstring(str, cstr, newStart, k, seen);

  /* Element chosen not to be part of the subset */
  cstr.erase(cstr.length() - 1);
  kSubstring(str, cstr, newStart, k, seen);
}

int main() {
  string s = "abcdefg";
  printSubsetOfString(s);
  return 0;
}

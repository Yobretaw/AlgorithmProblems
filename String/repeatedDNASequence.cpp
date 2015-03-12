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

long compress(const string& s);
int charToInt(const char& c);

/*
 *  All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
 *  for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
 *  
 *  Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
 *  
 *  For example,
 *  
 *  Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
 *  
 *  Return:
 *  ["AAAAACCCCC", "CCCCCAAAAA"].
 */
vector<string> findRepeatedDnaSequences(const string& s) {
  int len = s.length();
  if(len <= 10) return vector<string>();
  
  unordered_map<long, int> map;
  vector<string> result;
  long curr = compress(s.substr(0, 10));
  map[curr] = 1;

  for(int i = 10; i < len; ++i) {
    curr /= 10;
    curr += (long)(charToInt(s[i]) * pow(10, 9));

    if(map[curr]++ == 1) result.push_back(s.substr(i - 9, 10));
  }
  return result;
}

int charToInt(const char& c) {
  if(c == 'A') return 1;
  else if(c == 'T') return 2;
  else if(c == 'G') return 3;
  else return 4;
}

long compress(const string& s) {
  long ret = 0;
  for(int i = 9; i >= 0; --i) {
    ret *= 10;
    char c = s[i];
    if(c == 'A') ret += 1;
    else if(c == 'T') ret += 2;
    else if(c == 'G') ret += 3;
    else if(c == 'C') ret += 4;
  }
  cout << ret << endl;
  return ret;
}

int main() {
  string s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
  vector<string> result = findRepeatedDnaSequences(s);
  for(auto s : result) cout << s << endl;
  return 0;
}

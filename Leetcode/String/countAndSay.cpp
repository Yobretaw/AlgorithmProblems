#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <sstream>
#include <unordered_map>
using namespace std;

string getNext(const string& s);

/* The count-and-say sequence is the sequence of integers begining as follows:
 *
 * 1, 11, 21, 1211, 111221, ...
 * 
 * 1 is read off as "one 1" or 11
 * 11 is read off as "two 1s" or 21
 * 21 is read off as "one 2", then "one 1" or 1211
 *
 * Given an integer n, generate the nth sequence.
 * 
 * Note: The sequence of integers will be represented as a string.
 */
string countAndSay(int n) {
  string result = "1";
  while(--n)
    result = getNext(result);
  
  return result;
}

string getNext(const string& s) {
  stringstream ss;

  char c = s[0];
  for (int i = 1; i <= s.length(); ++i) {
    int j = i;
    while(j < s.length() && s[j] == c) j++;

    ss << (j - i + 1) << c;

    c = s[j];
    i = j;
  }
  return ss.str();
}

int main() {
  cout << countAndSay(1) << endl;
  return 0;
}

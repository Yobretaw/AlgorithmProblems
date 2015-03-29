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

/*
 *  Given two numbers represented as strings, return multiplication of the numbers as a string.
 *  
 *  Note: The numbers can be arbitrarily large and are non-negative.
 */
vector<int> toArray(string a) {
  vector<int> ret(a.length());
  for(int i = 0; i < a.length(); ++i)
    ret[a.length() - i - 1] = a[i] - '0';

  return ret;
}

string toString(const vector<int>& a) {
  string ret = "";
  int i = a.size() - 1;
  while(a[i] == 0) i--;
  while(i >= 0) ret += a[i--] + '0';
  return ret;
}

vector<int> multiplyHelp(const vector<int>& a, const vector<int>& b) {
  vector<int> ret(a.size() + b.size());
  for(int i = 0; i < a.size(); ++i) {
    for (int j = 0; j < b.size(); ++j) {
      ret[i + j] += a[i] * b[j];
      ret[i + j + 1] += ret[i + j] / 10;
      ret[i + j] %= 10;
    }
  }
  return ret;
}

string multiplyString(string a, string b) {
  //if(a == "0" || b == "0") return "0";
  return toString(multiplyHelp(toArray(a), toArray(b)));
}

int main() {
  cout << multiplyString("98", "98073984983274") << endl;
  return 0;
}

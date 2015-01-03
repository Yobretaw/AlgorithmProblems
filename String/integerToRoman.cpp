#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

/* Given an integer, convert it to a roman numberal.
 *
 * Input is guaranteed to be with the range from 1 to 3999
 */
string intToRoman(int n) {
  vector<string> symbols = {
    "I",  /* 1    */
    "V",  /* 5    */
    "X",  /* 10   */
    "L",  /* 50   */
    "C",  /* 100  */
    "D",  /* 500  */
    "M"   /* 1000 */
  };

  vector<int> values = { 1, 5, 10, 50, 100, 500, 1000 };

  string ret = "";
  bool pre = 0;
  for (int i = symbols.size() - 1; i >= 0; --i) {
    int curr = n / values[i];
    n %= values[i];

    if(curr == 4) {
      if(pre) {
        ret[ret.length() - 1] = symbols[i].c_str()[0];
        ret += symbols[i + 2];
      } else {
        ret += symbols[i];
        ret += symbols[i + 1];
      }
    } else {
      for (int j = 0; j < curr; ++j) {
        ret += symbols[i];
      }
    }
    pre = curr;
  }

  return ret;
}

string intToRoman2(int n) {
  static vector<pair<int, string> > valToSym = {
    make_pair(1    , "I"),
    make_pair(4    , "IV"),
    make_pair(5    , "V"),
    make_pair(9    , "IX"),
    make_pair(10   , "X"),
    make_pair(40   , "XL"),
    make_pair(50   , "L"),
    make_pair(90   , "XC"),
    make_pair(100  , "C"),
    make_pair(400  , "CD"),
    make_pair(500  , "D"),
    make_pair(900  , "CM"),
    make_pair(1000 , "M")
  };

  for(int i = valToSym.size() - 1; i >= 0; --i) {
    if(n >= valToSym[i].first)
      return valToSym[i].second + intToRoman2(n - valToSym[i].first);
  }

  return "";
}

int romanToInt(string s) {
  unordered_map<char, int> map;

  map['I'] = 1;
  map['V'] = 5;
  map['X'] = 10;
  map['L'] = 50;
  map['C'] = 100;
  map['D'] = 500;
  map['M'] = 1000;

  int result = 0;
  for (int i = 0; i < s.length(); ++i) {
    if(i > 0 && map[s[i]] > map[s[i - 1]])
      result += map[s[i]] - 2 * map[s[i - 1]];
    else
      result += map[s[i]];
  }

  return result;
}

int main() {
  //cout << intToRoman2(1904) << endl;
  //cout << intToRoman2(1954) << endl;
  //cout << intToRoman2(1990) << endl;
  //cout << intToRoman2(2014) << endl;
  for (int i = 0; i < 4000; ++i) {
    string s = intToRoman(i);
    int rev = romanToInt(s);
    cout << i << " : " << s << " : " << rev << endl;
  }
  return 0;
}

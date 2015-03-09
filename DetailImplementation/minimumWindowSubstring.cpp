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
 *  Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
 *  
 *  For example,
 *    S = "ADOBECODEBANC"
 *    T = "ABC"
 *  
 *  Minimum window is "BANC".
 *  
 *  Note:
 *    If there is no such window in S that covers all characters in T, return the emtpy string "".
 *  
 *    If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
 *    
 *  双指针，动态维护一个区间。尾指针不断往后扫，当扫到有一个窗口包含了所有T的字符后，
 *  然后再收缩头指针，直到不能再收缩为止。最后记录所有可能的情况中窗口最小的
 */
string findWindow(string s, string t) {
  if(s.empty()) return "";
  if(s.length() < t.length()) return "";

  vector<int> appeared_count(256, 0);
  vector<int> expected_count(256, 0);

  for(auto c : t) expected_count[c]++;

  int minWidth = INT_MAX, min_start = 0;
  int wnd_start = 0;    // 头指针
  int appeared = 0;     // 完整地包含一个T
  for(int wnd_end = 0; wnd_end < s.length(); ++wnd_end) {
    if(expected_count[s[wnd_end]] > 0) {
      appeared_count[s[wnd_end]]++;
      if(appeared_count[s[wnd_end]] <= expected_count[s[wnd_end]])
        appeared++;
    }
    if(appeared == t.length()) {    // 完整地包含了一个T
      // 收缩头指针
      while(appeared_count[s[wnd_start]] > expected_count[s[wnd_start]]
          || expected_count[s[wnd_start]]  == 0) {
         appeared_count[s[wnd_start]]--;
         wnd_start++;
      }
      if(minWidth > (wnd_end - wnd_start + 1)) {
        minWidth = wnd_end - wnd_start + 1;
        min_start = wnd_start;
      }
    }
  }
  
  if(minWidth == INT_MAX) return "";
  return s.substr(min_start, minWidth);
}

int main() {
  cout << findWindow("ADOBECODEBANC", "CABC") << endl;
  return 0;
}

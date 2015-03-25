#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
#include <unordered_set>
using namespace std;

/*
 *                                           1. Two Sum
 *  
 *  Given an array of integers, find two numbers such that they add up to a specific target number.
 *  
 *  The function twoSum should return indices of the two numbers such that they add up to the target,
 *  where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
 *  
 *  You may assume that each input would have exactly one solution.
 *  
 *  Input: numbers={2, 7, 11, 15}, target=9
 *  Output: index1=1, index2=2
 */
vector<int> twoSum(const vector<int>& numbers, int target) {
  unordered_map<int, int> mem;    // num -> idx
  vector<int> result(2);
  for(int i = 0; i < numbers.size(); ++i) {
    int curr = numbers[i];
    if(mem.count(target - curr)) {
      result[0] = mem[target - curr] + 1;
      result[1] = i + 1;
    } else {
      mem[curr] = i;
    }
  }
  return result;
}

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

/*
 *                                        2. Add Two Numbers
 *  You are given two linked lists representing two non-negative numbers. The digits are stored
 *  in reverse order and each of their nodes contain a single digit. Add the two numbers and return
 *  it as a linked list.
 *  
 *  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 *  Output: 7 -> 0 -> 8
 */
ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
  if(l1 == NULL && l2 == NULL) return NULL;
  if(l1 == NULL || l2 == NULL) return l1 == NULL ? l2 : l1;
  
  ListNode dummy(0);
  ListNode *curr = &dummy;
  
  int carry = 0;
  for(; l1 != NULL && l2 != NULL; l1 = l1->next, l2 = l2->next, curr = curr->next) {
    int val = l1->val + l2->val + carry;
    curr->next = new ListNode(val % 10);
    carry = val / 10;
  }

  ListNode *rest = l1 == NULL ? l2 : l1;
  for(; rest != NULL; rest = rest->next, curr = curr->next) {
    curr->next = new ListNode((rest->val + carry) % 10);
    carry = (rest->val + carry) / 10;
  }
  if(carry == 1) curr->next = new ListNode(1);
  return dummy.next;
}

ListNode* vectorToList(const vector<int>& arr) {
  ListNode dummy(0);
  ListNode *curr = &dummy;
  for(int i = 0; i < arr.size(); ++i) {
    curr->next = new ListNode(arr[i]);
    curr = curr->next;
  }
  return dummy.next;
}

vector<int> listToVector(ListNode *head) {
   vector<int> result;
   while(head) {
     result.push_back(head->val);
     head = head->next;
   }
   return result;
}

/*
 *                    3. Longest Substring Without Repeating Characters 
 *  
 *  Given a string, find the length of the longest substring without repeating characters.
 *  For example, the longest substring without repeating letters for "abcabcbb" is "abc", which
 *  the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
 */
int lengthOfLongestSubstring(string s) {
  const int TOTAL_CHAR = 256;
  vector<int> pos(TOTAL_CHAR, -1);
  int start = 0;
  int longest_start = 0, longest_len = 0;
  for(int i = 0; i < s.length(); ++i) {
    if(pos[s[i]] >= start) {
      start = pos[s[i]] + 1;
    }

    pos[s[i]] = i;

    if(i - start >= longest_len) {
      longest_start = start;
      longest_len = i - start + 1;
    }
  }
  //cout << s.substr(longest_start, longest_len) << endl;
  return longest_len;
}

/*
 *                                    4. Median of Two Sorted Arrays 
 *  
 *  There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
 *  The overall run time complexity should be O(log (m+n)).
 */


/*
 *                                    5. Longest Palindromic Substring
 *  
 *  Given a string S, find the longest palindromic substring in S. You may assume that the
 *  maximum length of S is 1000, and there exists one unique longest palindromic substring.
 */
string longestPalSubstring(const string& s) {
  int len = s.length();
  if(len < 2) return s;

  int maxstart = 0, maxlen = 1;
  string ret = "";
  vector<vector<bool> > mem(len, vector<bool>(len, false));

  //for(int i = 0; i < len; ++i)
  //  mem[i][i] = true;

  //for(int i = 0; i < len - 1; ++i) {
  //  if(s[i] == s[i + 1]) {
  //    mem[i][i + 1] = true;
  //    maxstart = i;
  //    maxlen = 2;
  //  }
  //}

  //for(int k = 3; k <= len; ++k) {
  //  for(int i = 0; i < len - k + 1; ++i) {
  //    int j = i + k - 1;
      
  //    if(s[i] == s[j] && mem[i + 1][j - 1])
  //      mem[i][j] = true;

  //    if(mem[i][j] && j - i + 1 > maxlen) {
  //      maxstart = i;
  //      maxlen = j - i + 1;
  //    }
  //  }
  //}
  
  for(int i = len - 1; i >= 0; --i) {
    for(int j = i; j < len; ++j) {
      mem[i][j] = s[i] == s[j] && (j - i < 2 || mem[i + 1][j - 1]);
      if(mem[i][j]) {
        if(j - i + 1 > maxlen) {
          maxlen = j - i + 1;
          maxstart = i;
        }
      }
    }
  }
  return s.substr(maxstart, maxlen);
}

string longestPalSubstring2(string s) {
  if(s.length() < 2) return s;

  // preprocessing
  string str = "#";
  for(int i = 0; i < s.length(); ++i) {
    str += s[i];
    str += "#";
  }

  int n = str.length();
  int f[n];
  int mid = 0, right = 0, pos = 0, len = 1;
  for(int i = 1; i < n; ++i) {
    if(right > i)
      f[i] = min(f[2 * mid - i], right - i);
    else
      f[i] = 0;

    while(i - f[i] - 1 >= 0 &&
          i + f[i] + 1 < n &&
          str[i - f[i] - 1] == str[i + f[i] + 1])
      f[i]++;

    if(len < f[i]) {
      len = f[i];
      pos = (i - f[i]) / 2;
    }
    if(right < i + f[i]) {
      mid = i;
      right = i + f[i];
    }
  }
  return s.substr(pos, len);
}

/*
 *                                  6. ZigZag Conversion
 */

/*
 *                                  7. Reverse Integer
 */
int reverseInteger(int x) {
  int sign = x < 0 ? -1 : 1;
  x *= sign;

  int ret = 0;
  while(x > 0) {
    if(INT_MAX / 10 < ret)
      return 0;

    ret *= 10;
    ret += x % 10;
    x /= 10;
  }
  return ret * sign;
}


/*
 *                                  7. String to Integer
 */
int stringToInteger(const string& s) {
  int n = s.length();
  if(n == 0) return 0;
  if(n == 1) return s[0] <= '9' && s[0] >= '0' ? s[0] - '0' : 0;

  int val = 0;
  int sign = 1;
  int idx = 0;

  // skip whitespaces
  while(s[idx] == ' ') idx++;    

  // all whitespaces
  if(idx == n) return 0;

  if(s[idx] == '+' || s[idx] == '-') {
    sign = s[idx] == '+' ? 1 : -1;
    idx++;
  }

  char c;
  while(idx < n && s[idx] >= '0' && s[idx] <= '9') {
    c = s[idx];
    int next = c - '0';

    if(sign > 0 && ((INT_MAX / 10 < val) || (INT_MAX / 10 == val && next > INT_MAX % 10)))
      return INT_MAX;
    else if(sign < 0 && ((INT_MIN / 10 > -val) || (INT_MIN / 10 == -val && -next < INT_MIN % 10)))
      return INT_MIN;

    val *= 10;
    val += next;
    idx++;
  }
  return val * sign;
}

int strStr(string haystack, string needle) {
  int hl = haystack.length();
  int nl = needle.length();

  if(nl == 0) return -1;

  int curr = 0;
  while(curr <= hl - nl) {
    if(haystack[curr] != needle[0]) {
      curr++;
    } else {
      int l = curr;
      int i = 0;
      while(i < nl && haystack[l] == needle[i]) {
        i++;
        l++;
      }
      if(i == nl) return r;
    }
  }
}

int main() {
  //cout << stringToInteger("-1") << endl;
  //cout << stringToInteger("-2147483641") << endl;
  return 0;
}

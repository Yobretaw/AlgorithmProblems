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
 *                                    5. Palindrome Number
 */
bool isPalindrome(int x) {
  if(x == 0) return true;
  if(x < 0) return false;

  int m = 1;
  while(x / m >= 10) m *= 10;
  while(x > 0) {
    if(x / m != x % 10) return false;

    x = (x % m) / 10;
    m /= 100;
  }
  return true;
}

/*
 *                                    10. Regular Expression Matching
 */
bool isMatch(const char* s, const char* p) {
  return false;
}


/*
 *                                    11. Container With Most Water
 */
int maxArea(const vector<int>& heights) {
  int n = heights.size();
  if(n < 2) return 0;

  int start = 0, end = n - 1;
  int maxArea = 0;

  while(start < end) {
    maxArea = max(maxArea, (end - start) * min(heights[start], heights[end]));
    heights[start] < heights[end] ? start++ : end--;
  }
  return maxArea;
}

/*
 *                                    12. Integer to Roman
 */

string intToRoman(int num) {
  unordered_map<int, string> m;

  m[1] = "I";
  m[4] = "IV";
  m[5] = "V";
  m[9] = "IX";
  m[10] = "X";
  m[40] = "XL";
  m[50] = "L";
  m[90] = "XC";
  m[100] = "C";
  m[400] = "CD";
  m[500] = "D";
  m[900] = "CM";
  m[1000] = "M";

  string ret = "";
  int d = 1;
  while(num / 10 >= d) d *= 10;

  while(num > 0) {
    int curr = num / d;
    if(curr == 9) {
      ret += m[9 * d];
    } else if(curr >= 5) {
      ret += m[5 * d];
      ret += string(curr - 5, m[d][0]);
    } else if(curr == 4){
      ret += m[4 * d];
    } else {
      ret += string(curr, m[d][0]);
    }
    num -= (num / d) * d;
    d = d / 10;
  }
  return ret;
}

int romanToInt(string s) {
  int len = s.length();
  if(len == 0) return 0;

  static unordered_map<char, int> m;
  
  m['I'] = 1;
  m['V'] = 5;
  m['X'] = 10;
  m['L'] = 50;
  m['C'] = 100;
  m['D'] = 500;
  m['M'] = 1000;

  int ret = m[s[0]];
  for(int i = 1; i < len; ++i) {
    int curr = m[s[i]];
    int prev = m[s[i - 1]];

    if(curr > prev) {
      ret -= 2 * prev;
      ret += curr;
    } else {
      ret += curr;
    }
  }
  return ret;
}

string longestCommonPrefix(vector<string> &strs) {
  int n = strs.size();        

  if(n == 0) return "";
  if(n == 1) return strs[0];

  sort(strs.begin(), strs.end());
  int len = strs[0].length();

  for(int i = 1; i < n; ++i) {
    string prev = strs[i - 1];
    string curr = strs[i];

    int l = 0;
    while(l < prev.length() && l < curr.length() && prev[l] == curr[l]) l++;
    len = min(l, len);
  }
  return strs[0].substr(0, len);
}

//////////////////////////////////////////////////////////
//                      15. 3 Sum
//////////////////////////////////////////////////////////
bool seen(unordered_map<int, unordered_map<int, int> >& mem, int key1, int key2) {
  return mem.count(key1) && mem[key1].count(key2);
}

void sumHelp(vector<int>& num, int start, int end, unordered_map<int, unordered_map<int, int> >& mem, vector<vector<int> >& result) {
  if(start >= end - 1 || seen(mem, num[start], num[end]))
    return;
  
  while(start < end - 2 && num[start] == num[start + 1] && num[start] == num[start + 2]) {
    start++;
  }

  while(start < end - 2 && num[end] == num[end - 1] && num[end] == num[end - 2]) {
    end--;
  }

  int j = start + 1;
  int sum;
  while(start < j && j < end) {
    sum = num[start] + num[end];
    if(num[j] == -sum) {
      if(!seen(mem, num[start], num[end])) {
        result.push_back(vector<int>{ num[start], num[j], num[end] });
        mem[num[start]][num[end]] = 1;
      }
    }
    j++;
  }

  mem[num[start]][num[end]] = 1;
  sumHelp(num, num[start] == num[start + 1] ? start + 2 : start + 1, num[end] == num[end - 1] ? end - 1 : end, mem, result);
  sumHelp(num, num[start] == num[start + 1] ? start + 1 : start, num[end] == num[end - 1] ? end - 2 : end - 1, mem, result);
}

vector<vector<int> > threeSum(vector<int> &num) {
  int n = num.size();

  vector<vector<int> > result;

  sort(num.begin(), num.end());

  if(n < 3) return result;
  if(n == 3) return num[0] + num[1] + num[2] == 0 ? vector<vector<int> >{ num } : result;

  unordered_map<int, unordered_map<int, int> > mem;
  sumHelp(num, 0, n - 1, mem, result);
  return result;
}

vector<vector<int> > threeSum2(vector<int> &num) {  
  vector<vector<int> > result;
  int len = num.size();

  sort(num.begin(), num.end());
  for(int i = 0; i < len; i++) {
    int target = -num[i];
    int start = i + 1, end = len - 1;
    while(start < end) {
      if(num[start] + num[end] == target) {
        result.push_back(vector<int>{num[i], num[start], num[end]});  
        start++;
        end--;  
        while(start < end && num[start] == num[start-1]) start++;  
        while(start < end && num[end] == num[end+1]) end--;  
      } else if(num[start] + num[end] < target) {
        start++;
      } else {
        end--;
      }
    }
    if(i < len-1)
      while(num[i] == num[i+1]) i++;
  }
  return result;
}

int main() {
  //vector<int> num = {-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1};
  //vector<int> num = {-1, 0, 1, 2, -1, -4};
  //vector<int> num = {0, 0, 0, 0};
  vector<int> num(1000, 0);
  for(int i = 0; i < 1000; ++i) {
    num[i] = -500 + i;
  }
  vector<vector<int> > result = threeSum2(num);

  for(auto v : result) {
    for(auto num : v)
      cout << num << " ";
    cout << endl;
  }
  return 0;
}

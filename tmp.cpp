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

int main() {
  // 2
  //ListNode *l1 = vectorToList(vector<int>{3,1,0,0,1,9,0,1,6,1});
  //ListNode *l2 = vectorToList(vector<int>{5,5,8,6,2,5,8,2,6,1});
  //ListNode *result = addTwoNumbers(l1, l2);
  //for(auto val : listToVector(result)) cout << val;
  //cout << endl;
  

  // 3
  cout << lengthOfLongestSubstring("c") << endl; 
  cout << lengthOfLongestSubstring("abcabcbb") << endl; 
  return 0;
}

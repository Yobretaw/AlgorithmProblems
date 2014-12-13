#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

int search(const vector<int>& arr, int target) {
  int start = 0, end = arr.size() - 1;
  while(start < end) {
    int mid = start + (end - start) / 2;
    if(arr[mid] == target)
      return mid;

    if(arr[mid] < target)
      start = mid + 1;
    else
      end = mid;
  }

  return -1;
}

// return true if two sets are disjoint, false otherwise
// O(mlogn) where m < n
bool isDisjoint_binary_search(const vector<int>& s1, const vector<int>& s2) {
  vector<int> st1 = s1;
  vector<int> st2 = s2;

  sort(st1.begin(), st1.end());
  for (int i = 0; i < (int)st2.size(); ++i) {
    if(search(st1, st2[i]) != -1)
      return false;
  }

  return true;
}

// O(min(m, n))
bool isDisjoint_hash(const vector<int>& s1, const vector<int>& s2) {
  unordered_map<int, int> m;
  for (int i = 0; i < (int)s1.size(); ++i) {
    m[s1[i]] = 1;
  }

  for (int i = 0; i < (int)s2.size(); ++i) {
    if(m.count(s2[i]) != 0)
      return false;
  }

  return true;
}

int main() {
  vector<int> s1 = {12, 34, 11, 9, 3};
  vector<int> s2 = {7, 2, 9, 5};
  //cout << isDisjoint_binary_search(s1, s2) << endl;
  cout << isDisjoint_hash(s1, s2) << endl;
  return 0;
}

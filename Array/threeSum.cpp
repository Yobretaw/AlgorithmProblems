#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <assert.h>
#include <unordered_map>
using namespace std;

// Given an array of integers, find two numbers such that they
// add up to a specific target number
// 
// The functoin twoSum should return the indices of the two
// numbers, where indices1 must be less that indices2
// 
// You may assume each input would have exactly one solution
void twoSum(const vector<int>& arr, int target, int& idc1, int& idc2) {
  unordered_map<int, int> m;

  int len = arr.size();
  for (int i = 0; i < len; ++i) {
    int curr = arr[i];
    if(m.count(target - curr) != 0) {
      idc1 = m[target - curr];
      idc2 = i;
      
      return;
    }

    m[curr] = i;
  }

  idc1 = -1;
  idc2 = -1;
}


// The 3SUM problem asks if a given set of n integers, each with absolute value bounded by some polynomial in n, contains three elements that sum to zero.
void threeSum(vector<int> a) {
  unordered_map<int, int> m;
  for(int i = 0; i < (int)a.size(); ++i) {
    m[a[i]] = i;
  }

  for(int i = 0; i < (int)a.size() - 1; ++i) {
    for(int j = i + 1; j < (int)a.size(); ++j) {
      int val = -(a[i] + a[j]);
      if(m.count(val) == 1 && m[val] < i && i < j) {
        cout << val << " " << a[i] << " " << a[j] << endl;
      }
    }
  }
}

int closest_threeSum(const vector<int>& arr, int target) {
  assert(arr.size() >= 3);
  vector<int> A(arr);

  int len = A.size();
  sort(A.begin(), A.end());

  int mingap = INT_MAX;
  int result;
  for(auto a = A.begin(); a != prev(A.end(), 2); ++a) {
    auto b = next(a);
    auto c = prev(A.end());

    int sum = 0, gap = INT_MAX;
    while(b < c) {
      sum = *a + *b + *c;
      gap = abs(sum - target);

      if(gap < mingap) {
        result = sum;
        mingap = gap;
      }

      if(sum < target) ++b;
      else --c;
    }
  }

  return result;
}

int main()
{
  vector<int> a = { -25, -10, -7, -3, 2, 4, 8, 10 };
  //threeSum(a);
  cout << closest_threeSum(a, 13) << endl;

  //vector<int> b = { 2, 7, 11, 15 };

  //int idc1, idc2;
  //twoSum(b, 17, idc1, idc2);

  //if(idc1 == -1 || idc2 == -1) {
  //  cout << "TWO SUM NOT FOUND" << endl;
  //} else {
  //  cout << b[idc1] << " + " << b[idc2] << endl;
  //}
  return 0;
}

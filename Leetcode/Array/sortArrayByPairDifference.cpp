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
 * For example we have the array X[n] = {X0, X1, X2, ... Xn} The goal is to sort this array
 * that the absolute value of difference between every pair is in ascending order.
 * 
 * For example X[] = {1, 2, 10, 15, 40, 50, 60, 61, 100, 101};
 * 
 * Answers are:
 *  {50, 40, 60, 15, 61, 10, 100, 2, 101, 1}
 *    
 */
void sortByDiff(vector<int>& arr) {
  if(arr.empty()) return;

  sort(arr.begin(), arr.end());

  int n = arr.size();
  vector<int> tmp(arr.size(), 0);

  int mid = n / 2;
  tmp[0] = arr[mid];

  int idx = 1;
  int offset = -1;
  while(abs(offset) <= mid) {
    tmp[idx++] = arr[mid + offset];
    offset = -offset;
    if(offset + mid < n)
      tmp[idx++] = arr[mid + offset];
    offset = -offset - 1;
  }
  arr = tmp;
  return;
}

int main() {
  vector<int> a = {1, 2, 10, 15, 40, 50, 60, 61, 100, 101};
  //vector<int> a = {1, 2, 10, 15, 40, 50, 60, 61, 100, 101, 120};
  cout << a.size() << endl;
  sortByDiff(a);
  for (int i = 0; i < a.size(); ++i) {
    cout << a[i] << (i == a.size() - 1 ? " " : ", ");
    if(i > 0)
      cout << abs(a[i] - a[i - 1]) << endl;
    else
      cout << endl;
  }
  return 0;
}

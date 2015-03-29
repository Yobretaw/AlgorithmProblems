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

int searchInsertionPosition(const vector<int>& a, int x) {
  int n = a.size();
  int low = 0, high = n;

  int mid;
  while(low < high) {
    mid = (high - low) / 2 + low;
    if(a[mid] == x) return mid;
    else if(a[mid] < x) low = mid + 1;
    else high = mid;
  }
  return a[mid] > x ? mid : mid + 1;
}

int main() {
  vector<int> a = {1, 3, 5, 6};
  cout << searchInsertionPosition(a, 5) << endl;    // should output 2
  cout << searchInsertionPosition(a, 2) << endl;    // should output 1
  cout << searchInsertionPosition(a, 7) << endl;    // should output 4
  cout << searchInsertionPosition(a, 0) << endl;    // should output 0
  return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

int findSecondLargest(const vector<int>& arr) {
  int len = arr.size();
  int max = INT_MIN, secmax = INT_MIN;

  for(int i = 0; i < len; i++) {
    if(arr[i] > max)
      max = arr[i];

    if(arr[i] > secmax && arr[i] < max)
      secmax = arr[i];
  }

  return secmax;
}

int main() {
  vector<int> arr = {9, 8, 7, 6, 5, 5, 4, 3, 2, 1};
  cout << findSecondLargest(arr) << endl;
  return 0;
}

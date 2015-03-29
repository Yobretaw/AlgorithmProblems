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

void bucket_sort(vector<int>& arr);

//// this algorithm works only if arr contains on repeating elements
//int firstMissingPositive(const vector<int>& arr) {
//  int sum = 0;
//  int max = 0;
//  for (int i = 0; i < arr.size(); ++i) {
//    if(arr[i] <= 0) continue;
//    sum += arr[i];
//    if(arr[i] > max) max = arr[i];
//  }
//  int total = (1 + max) * max / 2;
//  if(total - sum > 0) {
//    return total - sum;
//  }
//  return max + 1;
//}

/* Given an unsorted integer array, find the first missing positive integer.
 * 
 * For example, given [1, 2, 0] return 3, and [3, 4, 1, -1] return 2
 * 
 * Your algorithm should run in O(n) time and use constant space
 */
int firstMissingPositive2(vector<int>& arr) {
  bucket_sort(arr);

  for (int i = 0; i < arr.size(); ++i)
    if(arr[i] != (i + 1))
      return i + 1;

  return arr.size() + 1;
}

void bucket_sort(vector<int>& arr) {
  for (int i = 0; i < arr.size(); ++i) {
    while(arr[i] != i + 1) {
      if(arr[i] <= 0 || arr[i] > arr.size() || arr[i] == arr[arr[i] - 1])
        break;
      swap(arr[i], arr[arr[i] - 1]);
    }
  }
}

int main() {
  vector<int> arr = {3, 4, 1, -1};
  //vector<int> arr = {1, 2, 0};
  cout << firstMissingPositive2(arr) << endl;
  return 0;
}

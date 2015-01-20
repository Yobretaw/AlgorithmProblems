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

/* Given an unsorted integer array, find the first missing positive integer.
 * 
 * For example, given [1, 2, 0] return 3, and [3, 4, 1, -1] return 2
 * 
 * Your algorithm should run in O(n) time and use constant space
 */
int firstMissingPositive(const vector<int>& arr) {
  int sum = 0;
  int max = 0;
  for (int i = 0; i < arr.size(); ++i) {
    if(arr[i] <= 0) continue;
    sum += arr[i];

    if(arr[i] > max) max = arr[i];
  }
  if((max * (max + 1)) / 2 > 0) {
    return (max * (max + 1)) / 2 - sum;
  }
  return max + 1;
}

int main() {
  vector<int> arr = {3, 4, 1, -1};
  cout << firstMissingPositive(arr) << endl;
  return 0;
}

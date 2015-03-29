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

/* Given a sorted array of integers, find the starting and
 * ending position of a given target value.
 *
 * Your algorithm’s runtime complexity must be in the order of O(log n).
 * 
 * If the target is not found in the array, return [-1, 1]
 * 
 * For example, given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4]
 */
pair<int, int> findRange(const vector<int>& a, int x) {
  int n = a.size();
  if(n == 0) return make_pair(-1, -1);

  int low = 0, high = n;
  int idx = -1;
  pair<int, int> result;

  while(low < high) {
    int mid = (high - low) / 2 + low;
    if(a[mid] == x){
      idx = mid;
      high--;
    }
    else if(a[mid] > x) high = mid;
    else low = mid + 1;
  }

  // not exist
  if(idx == -1) return make_pair(-1, -1);

  result.first = idx;
  low = 0, high = n;
  while(low < high) {
    int mid = (high - low) / 2 + low;
    if(a[mid] == x) {
      idx = mid;
      low++;
    }
    else if(a[mid] > x) high = mid;
    else low = mid + 1;
  }
  result.second = idx;
  return result;
}

int main() {
  vector<int> a = {5, 7, 7, 8, 8, 10};
  pair<int, int> result = findRange(a, 10);
  cout << result.first << endl;
  cout << result.second << endl;
  return 0;
}

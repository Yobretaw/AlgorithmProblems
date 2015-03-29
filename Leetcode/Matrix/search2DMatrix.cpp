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

/* Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has
 * the following properties:
 *    - Integers in each row are sorted from left to right
 *    - The first integer of each row is greater than the last integer of the previous row
 *
 * For example, consider the following matrix:
 * [
 *  [1,   3,  5,  7],
 *  [10, 11, 16, 20],
 *  [23, 30, 34, 50]
 * ]
 * 
 * Given target = 3, return true
 */
bool search(const vector<vector<int> >& matrix, int target) {
  if(matrix.empty()) return false;

  const int m = matrix.size();
  const int n = matrix[0].size();

  int first = 0, last = m * n;
  while(first < last) {
    int mid = (last - first) / 2 + first;
    int val = matrix[mid / n][mid % n];

    if(val == target) {
      return true;
    } else if(val < target) {
      first = mid + 1;
    } else {
      last = mid;
    }
  }
  return false;
}

int main() {
  vector<vector<int> > m = {
    {1, 3, 5, 7},
    {10, 11, 16, 20},
    {23, 30, 34, 50}
  };
  for (int i = 0; i < 50; ++i) {
    cout << i << ": " << search(m, i) << endl;
  }
  return 0;
}

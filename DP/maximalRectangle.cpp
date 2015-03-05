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

/* Given a 2D matrix filled with 0's and 1's, find the largest rectangle containing all
 * ones and return its area.
 */
int maxRectangle(vector<vector<int> >& mtx) {
  if(mtx.empty()) return 0;

  const int m = mtx.size();
  const int n = mtx[0].size();
  vector<int> height(n, 0);
  vector<int> L(n, 0);
  vector<int> R(n, n);

  int ret = 0;
  for (int i = 0; i < m; ++i) {
    int left = 0, right = n;

    // calculate L(i, j) from left to right
    for (int j = 0; j < n; ++j) {
      if(mtx[i][j] == '1') {
        height[j]++;
        L[j] = max(L[j], left);
      } else {
        left = j + 1;
        height[j] = 0;
        L[j] = 0;
      }
    }

    // calculate R(i, j) from right to left
    for(int j = n - 1; j >= 0; --j) {
      if(mtx[i][j] == '1') {
        R[j] = min(R[j], right);
        ret = max(ret, height[j] * (R[j] - L[j]));
      } else {
        right = j;
        R[j] = n;
      }
    }
  }
  return ret;
}

int main() {

  return 0;
}

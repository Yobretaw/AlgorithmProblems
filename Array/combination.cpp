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

void subsetHelpSizeK(int n, vector<int>& path, int step, vector<vector<int> >&result, int k);
/* find all combination of k integers from 1 to n.
 * 
 * Input n = 4 and k = 2,
 *
 * output
 *  [
 *    [1, 2],
 *    [1, 3],
 *    [1, 4],
 *    [2, 3],
 *    [2, 4],
 *    [3, 4]
 *  ]
 */
vector<vector<int> > combination(int n, int k) {
  vector<vector<int> > result;
  
  if(n == 0) return result;

  vector<int> set;
  subsetHelpSizeK(n, set, 1, result, k);
  return result;
}

void subsetHelpSizeK(int n, vector<int>& path, int step, vector<vector<int> >&result, int k) {
  // return if size reached k
  if(path.size() == k) {
    result.push_back(path);
    return;
  }

  // return if reach upper bound
  if(step == n + 1) return;

  // does not include a[setp]
  subsetHelpSizeK(n, path, step + 1, result, k);

  // includ a[step]
  path.push_back(step);
  subsetHelpSizeK(n, path, step + 1, result, k);

  path.pop_back();
}

int main() {
  int n = 5, k = 2;
  vector<vector<int> > result = combination(n, k);
  for (int i = 0; i < result.size(); ++i) {
    for (int j = 0; j < result[i].size(); ++j) {
      cout << result[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}

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
 * Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
 * 
 * For example, given the following triangle
 * [
 *      [2],
 *     [3,4],
 *    [6,5,7],
 *   [4,1,8,3]
 * ]
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
 * 
 * Note:
 * Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
 */
int minPath(const vector<vector<int> >& t) {
  int level = t.size();

  vector<vector<int> > mem(level, vector<int>(level, 0));
  mem[0][0] = t[0][0];
  for (int i = 1; i < level; ++i) {
    mem[i][0] = t[i][0] + mem[i - 1][0];
    mem[i][i] = t[i][i] + mem[i - 1][i - 1];
    for(int j = 1; j < i; ++j) {
      mem[i][j] = t[i][j] + min(mem[i - 1][j - 1], mem[i - 1][j]);
    }
  }
  int minval = mem[level - 1][0];
  for (int i = 0; i < level; ++i) {
    minval = min(minval, mem[level - 1][i]);
  }
  return minval;
}

int main() {
  vector<vector<int> > t = {
    {2},
    {3, 4},
    {6, 5, 7},
    {4, 1, 8, 3}
  };
  cout << minPath(t) << endl;
  return 0;
}

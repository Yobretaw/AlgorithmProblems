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
 *  Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
 *  Note: You can only move either down or right at any point in time.
 */
//void minPathHelp(const vector<vector<int> >& grid, int x, int y, vector<vector<int> >& mem) {
//  int m = grid.size();
//  int n = grid[0].size();

//  // reaching lower right corner
//  if(x == m - 1 && y == n - 1) return grid[x][y] + min(x == 0 ? 0 : mem[x - 1][y], y == 0 ? 0 : mem[x, y - 1]);

//  // already traversed
//  if(mem[x][y] >= 0) return mem[x][y];
//}

//int minPath(const vector<vector<int> >& grid) {
//  if(grid.size() == 0) return 0;

//  vector<vector<int> > mem(grid.size(), vector<int>(grid[0].size(), -1));
//  minPathHelp(grid, 0, 0, mem);
//  return mem[grid.size() - 1][grid[0].size() - 1];
//}

// 二维DP
int minPath2(const vector<vector<int> >& grid) {
  int m = grid.size();
  int n = grid[0].size();

  if(m == 0) return 0;

  vector<vector<int> > mem(m, vector<int>(n, -1));
  mem[0][0] = grid[0][0];

  for (int i = 1; i < m; ++i)
    mem[i][0] = mem[i - 1][0] + grid[i][0];

  for (int i = 1; i < n; ++i)
    mem[0][i] = mem[0][i - 1] + grid[0][i];

  for (int i = 1; i < m; ++i)
    for (int j = 1; j < n; ++j)
      mem[i][j] = grid[i][j] + min(mem[i - 1][j], mem[i][j - 1]);

  return mem[m - 1][n - 1];
}

// 滚动数组
int minPath3(const vector<int> >& grid) {
  int m = grid.size();
  int n = grid[0].size();

  if(m == 0) return 0;
  vector<int> mem(n, INT_MAX);
  mem[0] = 0;

  for (int i = 0; i < m; ++i) {
    mem[0] += grid[i][0];
    for (int j = 1; j < n; ++j) {
      mem[j] = grid[i][j] + min(mem[j], mem[j - 1]);
    }
  }

  return mem[n - 1];
}

int main() {
  return 0;
}

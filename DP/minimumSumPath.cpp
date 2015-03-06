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
int minPathHelp(const vector<vector<int> >& grid, int x, int y, vector<vector<int> >& mem) {
  if(x == 0 && y == 0) return grid[0][0];

  int m = grid.size();
  int n = grid[0].size();

  if(mem[x][y] >= 0) return mem[x][y];

  int left = -1, up = -1;
  if(x > 0)
    left = minPathHelp(grid, x - 1, y, mem);

  if(y > 0)
    up = minPathHelp(grid, x, y - 1, mem);

  mem[x][y] = grid[x][y] + min(left == -1 ? INT_MAX : left, up == -1 ? INT_MAX : up);
  return mem[x][y];
}

// Recursion
int minPath(const vector<vector<int> >& grid) {
  vector<vector<int> > mem(grid.size(), vector<int>(grid[0].size(), -1));
  return minPathHelp(grid, grid.size() - 1, grid[0].size() - 1, mem);
}

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
int minPath3(const vector<vector<int> >& grid) {
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
  vector<vector<int> > grid = {
    {0, 0},
    {0, 0}
  };

  cout << minPath(grid) << endl;
  return 0;
}

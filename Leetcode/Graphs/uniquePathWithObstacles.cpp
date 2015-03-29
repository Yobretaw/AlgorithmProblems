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


// time O(mn), space O(mn)
int uniquePath_help(int m, int n, const vector<vector<int> >& grid) {
  int x = grid.size();
  int y = grid[0].size();
  static vector<vector<int> > mem(x, vector<int>(y, -1));

  if(m == x - 1 && n == y - 1) return !grid[x - 1][y - 1];

  if(grid[m][n] == 1) {
    mem[m][n] = 0;
    return 0;
  }

  if(mem[m][n] >= 0) return mem[m][n];

  if(m == x - 1) mem[m][n] = uniquePath_help(m, n + 1, grid);
  else if(n == y - 1) mem[m][n] = uniquePath_help(m + 1, n, grid);
  else mem[m][n] = uniquePath_help(m + 1, n, grid) + uniquePath_help(m, n + 1, grid);

  return mem[m][n];
}

int uniquePath(const vector<vector<int> >& grid) {
  return uniquePath_help(0, 0, grid);
}

int uniquePath2(const vector<vector<int> >& grid) {
  if(grid.size() == 0) return 0;

  int m = grid.size();
  int n = grid[0].size();

  if(grid[0][0] || grid[m - 1][n - 1]) return 0;

  vector<int> mem(n, 0);
  mem[0] = 1;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      mem[j] = grid[i][j] ? 0 : (j == 0 ? 0 : mem[j - 1]) + mem[j];
    }
  }

  return mem[n - 1];
}

int main() {
  int m = 2;
  int n = 2;
  vector<vector<int> > grid(m, vector<int>(n, 0));
  grid[1][0] = 1;
  cout << uniquePath(grid) << endl;
  cout << uniquePath2(grid) << endl;
  return 0;
}

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
int uniquePath(int m, int n) {
  // grid of size m x n
  static vector<vector<int> > grid(m + 1, vector<int>(n + 1, -1));
  if(m == 1 && n == 1) return 1;
  if(grid[m][n] >= 0) return grid[m][n];

  if(m == 1) grid[m][n] = uniquePath(m, n - 1);
  else if(n == 1) grid[m][n] = uniquePath(m - 1, n);
  else grid[m][n] = uniquePath(m - 1, n) + uniquePath(m, n - 1);

  return grid[m][n];
}

// time O(mn), space O(n)
int uniquePath2(int m, int n) {
  vector<int> p(n, 0);
  p[0] = 1;

  for (int i = 0; i < m; ++i)
    for (int j = 1; j < n; ++j)
      // p[j]    =        p[j] +    p[j - 1]
      // f[i][j] = f[i - 1][j] + f[i][j - 1]
      p[j] += p[j - 1];

  return p[n - 1];
}

long factor(int start, int end) {
  long ret = 1;
  while(start <= end)
    ret *= start++;

  return ret;
}

// calculate n choose k
long combination(int n, int k) {
  if(k == 0) return 1;
  if(k == 1) return n;

  long ret = factor(k + 1, n); // n! / k!
  ret /= factor(1, n - k);    // n! / k!(n-k)!
  return ret;
}

long uniquePath3(int m, int n) {
  // top to down: m - 1 steps
  // left to right: n - 1 steps
  // total: m + n - 2 steps
  return combination(m + n - 2, m - 1);
}

int main() {
  //cout << uniquePath(10, 10) << endl;
  //cout << uniquePath(10, 12) << endl;
  //cout << uniquePath2(10, 12) << endl;
  //cout << uniquePath3(10, 12) << endl;
  return 0;
}

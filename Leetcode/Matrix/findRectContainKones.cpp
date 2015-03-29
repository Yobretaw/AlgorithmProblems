#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
using namespace std;

#define vi vector<int>
#define vvi vector<vector<int> >

/*
 * Given a matrix filled with 0s and 1s, find the number
 * of rectangles with length and height being a and b
 * respectively, and contains exactly k ones.
 *
 * Runtime: O(mn)
 * Space: O(mn)
 */
int find(const vvi& ma, int a, int b, int k) {
  int m = ma.size();
  int n = ma[0].size();
  int count = 0;

  // rowOnes[i][j] = ma[0][j] + ma[1][j] + .. + ma[i][j]
  // colOnes[i][j] = ma[i][0] + ma[i][1] + .. + ma[i][j]
  vvi rowOnes(m, vi(n, 0));
  vvi colOnes(m, vi(n, 0));

  // processing matrix and generate rowOnes and colOnes
  for(int i = 0; i < m; i++) {
    for(int j = 0; j < n; j++) {
      rowOnes[i][j] = i == 0 ? ma[i][j] : rowOnes[i-1][j] + ma[i][j];
      colOnes[i][j] = j == 0 ? ma[i][j] : colOnes[i][j-1] + ma[i][j];
    }
  }

  int topOnes = 0;
  int countOnes = 0;

  // calculate # of ones in the top left rectangle
  for(int i = 0; i < a; i++) {
    topOnes += colOnes[i][b-1];
  }

  for(int row = 0; row <= m - a; row++) {
    int removeRow = row - 1;
    int addRow = row + a - 1;

    // if row == 0 then don't add/sub from topOnes
    topOnes -= row == 0 ? 0 : colOnes[removeRow][b - 1];
    topOnes += row == 0 ? 0 : colOnes[addRow][b - 1];

    countOnes = topOnes;
    if(countOnes == k) count++;

    for(int col = 1; col <= n - b; col++) {
      int removeCol = col - 1;
      int addCol = col + b - 1;

      countOnes -= rowOnes[addRow][removeCol] - (row == 0 ? 0 : rowOnes[removeRow][removeCol]);
      countOnes += rowOnes[addRow][addCol] - (row == 0 ? 0 : rowOnes[removeRow][addCol]);

      if(countOnes == k) count++;
    }
  }

  return count;
}

int main() {
  vvi m = {
    {1, 0, 0, 1},
    {0, 1, 1, 0},
    {1, 0, 1, 1},
    {1, 0, 1, 0}
  };

  cout << find(m, 3, 3, 5) << endl;
  return 0;
}

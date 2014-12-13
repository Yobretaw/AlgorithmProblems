#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
using namespace std;

/*
 * Given a matrix filled with 0s and 1s, find the number
 * of rectangles with length and height being a and b
 * respectively, and contains exactly k ones.
 *
 * Runtime: O(mn)
 * Space: O(mn)
 */
int find(const vector<vector<int> >& ma, int a, int b, int k) {
  int m = ma.size();
  int n = ma[0].size();
  int count = 0;

  // rowOnes[i][j] = ma[0][j] + ma[1][j] + .. + ma[i][j]
  // colOnes[i][j] = ma[i][0] + ma[i][1] + .. + ma[i][j]
  int rowOnes[m][n];
  int colOnes[m][n];

  // Initialization: set to 0
  for(int i = 0; i < m; i++) {
    for(int j = 0; j < n; j++) {
      rowOnes[i][j] = 0;
      colOnes[i][j] = 0;
    }
  }

  // processing ma
  for(int i = 0; i < m; i++) {
    for(int j = 0; j < n; j++) {
      rowOnes[i][j] = i == 0 ? ma[i][j] : rowOnes[i-1][j] + ma[i][j];
      colOnes[i][j] = j == 0 ? ma[i][j] : colOnes[i][j-1] + ma[i][j];
    }
  }

  int tmp = 0;
  int countOnes = 0;
  for(int i = 0; i < a; i++)
    tmp += colOnes[i][b-1];
  if(tmp == k)
    count++;

  countOnes = tmp;
  for(int row = 0; row <= m - a; row++) {
    int removeRow = row - 1;
    int addRow = row + a - 1;

    if(row != 0) {
      tmp -= colOnes[removeRow][b - 1];
      tmp += colOnes[addRow][b - 1];

      countOnes = tmp;
      if(countOnes == k)
        count++;
    }

    for(int col = 1; col <= n - b; col++) {
      int removeCol = col - 1;
      int addCol = col + b - 1;

      countOnes -= (rowOnes[addRow][removeCol] - (row == 0 ? 0 : rowOnes[removeRow][removeCol]));
      countOnes += (rowOnes[addRow][addCol] - (row == 0 ? 0 : rowOnes[removeRow][addCol]));

      if(countOnes == k) count++;
    }
  }

  return count;
}

int main() {
  vector<vector<int > > m = {
    {1, 0, 0, 1},
    {0, 1, 1, 0},
    {1, 0, 1, 1},
    {1, 0, 1, 0}
  };

  cout << find(m, 3, 3, 5) << endl;
  return 0;
}

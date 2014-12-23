#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

#define N 9

bool isValidSudoku(int su[N][N]) {
  for (int i = 0; i < N; i++) {
    // check row
    int seen[N] = {0};
    for(int j = 0; j < N; j++) {
      if(seen[su[i][j]-1] == 1)
        return false;

      seen[su[i][j]-1] = 1;
    }

    // check col
    for (int j = 0; j < N; j++) {
      if(seen[su[j][i] - 1] == 0)
        return false;

      seen[su[j][i] - 1] = 0;
    }
  }

  for(int i = 1; i < N - 1; i+=3) {
    for(int j = 1; j < N - 1; j+=3) {
      int seen[N] = {0};
      for(int x = -1; x < 2; ++x) {
        for (int y = -1; y < 2; ++y) {
          if(seen[su[i + x][j + y] - 1]) {
            return false;
          }
          seen[su[i+x][j+y] - 1] = 1;
        }
      }
    }
  }

  return true;
}

int main() {
  int grid[N][N] = {
    {3,1,6,5,7,8,4,9,2},
    {5,2,9,1,3,4,7,6,8},
    {4,8,7,6,2,9,5,3,1},
    {2,6,3,4,1,5,9,8,7},
    {9,7,4,8,6,3,1,2,5},
    {8,5,1,7,9,2,6,4,3},
    {1,3,8,9,4,7,2,5,6},
    {6,9,2,3,5,1,8,7,4},
    {7,4,5,2,8,6,3,1,9},
  };

  cout << isValidSudoku(grid) << endl;
  return 0;
}

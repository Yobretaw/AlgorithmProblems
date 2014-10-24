#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

#define N 8

void printGrid(int grid[N][N]) {
    for (int row = 0; row < N; row++)
    {
       for (int col = 0; col < N; col++)
             printf("%2d", grid[row][col]);
        printf("\n");
    }
    cout << endl;
}


bool isSave(int grid[N][N], int row, int col) {
  // check columns only
  for (int i = 0; i < N; i++) {
    if(grid[i][col] == 1)
      return false;
  }

  // check upper diagonal
  int i = row - 1, j = col - 1;
  while(i >= 0 && j >= 0)
    if(grid[i--][j--] == 1)
      return false;

  // check lower diagonal
  i = row + 1, j = col + 1;
  while(i < N && j < N)
    if(grid[i++][j++] == 1)
      return false;

  return true;
}

bool solve(int grid[N][N], int level) {
  if(level == N) {
    return true;
  }

  for (int i = 0; i < N; i++) {
    if(!isSave(grid, level, i)) {
      continue;
    }

    grid[level][i] = 1;

    if(solve(grid, level + 1)) {
      return true;
    }

    grid[level][i] = 0;
  }

  return false;
}

int main()
{
  int grid[N][N];
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      grid[i][j] = 0;
    }
  }

  solve(grid, 0);
  printGrid(grid);
  return 0;
}

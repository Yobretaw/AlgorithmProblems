#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <stack>
using namespace std;

#define N 9

bool isSafe(int su[N][N], int row, int col, int num);
bool findUassignedLocation(vector<vector<int> > su, int& row, int& col);
bool solve(int su[N][N]);
void printGrid(int grid[N][N]);

bool isSafe(int su[N][N], int row, int col, int num) {
  // check same number in row
  for(int i = 0; i < N; i++)
    if(su[row][i] == num)
      return false;

  // check same number in col 
  for(int i = 0; i < N; i++)
    if(su[i][col] == num)
      return false;

  // check same number is box of 3x3
  int rowStart = row - row % 3;
  int colStart = col - col % 3;
  for(int i = 0; i < 3; i++)
    for(int j = 0; j < 3; j++)
      if(su[rowStart + i][colStart + j] == num)
        return false;

  return true;
}

bool findUassignedLocation(int su[N][N], int& row, int& col) {
  for(row = 0; row < N; row++)
    for(col = 0; col < N; col++)
      if(su[row][col] == 0)
        return true;

  return false;
}



bool solve(int su[N][N]) {
  int row, col;

  if(!findUassignedLocation(su, row, col)) {
    return true;
  }

  for (int i = 1; i <= N; i++) {
    if(isSafe(su, row, col, i)) {
      su[row][col] = i;

      if(solve(su)) {
        return true;
      }

      su[row][col] = 0;
    }
  }

  return false;
}

void printGrid(int grid[N][N]) {
    for (int row = 0; row < N; row++)
    {
       for (int col = 0; col < N; col++)
             printf("%2d", grid[row][col]);
        printf("\n");
    }
}

int main(int argc, const char *argv[])
{
  int grid[N][N] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                    {5, 2, 0, 0, 0, 0, 0, 0, 0},
                    {0, 8, 7, 0, 0, 0, 0, 3, 1},
                    {0, 0, 3, 0, 1, 0, 0, 8, 0},
                    {9, 0, 0, 8, 6, 3, 0, 0, 5},
                    {0, 5, 0, 0, 9, 0, 6, 0, 0},
                    {1, 3, 0, 0, 0, 0, 2, 5, 0},
                    {0, 0, 0, 0, 0, 0, 0, 7, 4},
                    {0, 0, 5, 2, 0, 6, 3, 0, 0}};

  if(solve(grid)) {
    printGrid(grid);
  } else {
    cout << "NO SOLUTION FOUND!" << endl;
  }
  return 0;
}

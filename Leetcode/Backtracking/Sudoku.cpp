#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <unordered_set>
#include <utility>      // std::pair
#include <ctime>
#include <numeric>
using namespace std;

#define N 9
#define ENABLE_FORWARD_CHECKING false

bool isSafe(int su[N][N], int row, int col, int num, int rows[N], int cols[N], int boxes[N]);
bool findUassignedLocation(int su[N][N], int& row, int& col, vector<pair<int, int> >& emptys);
bool solve(int su[N][N], int rows[N], int cols[N], int boxes[N], vector<pair<int, int> >& emptys);
void printGrid(int grid[N][N]);

int IDX_TO_PRIME[9] = {2, 3, 5, 7, 11, 13 ,17, 19, 23};

bool isSafe(int su[N][N], int row, int col, int num, int rows[N], int cols[N], int boxes[N]) {
  num = IDX_TO_PRIME[num - 1];
  bool res = rows[row] % num != 0 && cols[col] % num != 0 && boxes[row - row % 3 + col / 3] % num != 0;
  return res;
}

bool findUassignedLocation(int su[N][N], int& row, int& col, vector<pair<int, int> >& emptys) {
  if(emptys.empty()) return false;
  row = emptys[emptys.size() - 1].first;
  col = emptys[emptys.size() - 1].second;
  return true;
}

bool solve(int su[N][N], int rows[N], int cols[N], int boxes[N], vector<pair<int, int> >& emptys) {
  int row, col;

  if(!findUassignedLocation(su, row, col, emptys)) {
    return true;
  }

  emptys.pop_back();
  for (int i = 1; i <= N; i++) {
    if(isSafe(su, row, col, i, rows, cols, boxes)) {
      su[row][col] = i;

      int d = IDX_TO_PRIME[i - 1];
      rows[row] *= d;
      cols[col] *= d;
      boxes[row - row % 3 + col / 3] *= d;

      if(solve(su, rows, cols, boxes, emptys)) {
        return true;
      }

      rows[row] /= d;
      cols[col] /= d;
      boxes[row - row % 3 + col / 3] /= d;
      su[row][col] = 0;
    }
  }
  emptys.push_back(pair<int, int>(row, col));
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
  int count = 0;
  int nums = 500;
  vector<double> times(nums);
  for(int i = 0; i < nums; ++i) {
    clock_t start = clock();
    //int grid[N][N] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
    //                  {5, 2, 0, 0, 0, 0, 0, 0, 0},
    //                  {0, 8, 7, 0, 0, 0, 0, 3, 1},
    //                  {0, 0, 3, 0, 1, 0, 0, 8, 0},
    //                  {9, 0, 0, 8, 6, 3, 0, 0, 5},
    //                  {0, 5, 0, 0, 9, 0, 6, 0, 0},
    //                  {1, 3, 0, 0, 0, 0, 2, 5, 0},
    //                  {0, 0, 0, 0, 0, 0, 0, 7, 4},
    //                  {0, 0, 5, 2, 0, 6, 3, 0, 0}};

    int grid[N][N] = {
      {3, 0, 9, 0, 0, 0, 0, 4, 2,},
      {0, 1, 8, 9, 4, 3, 6, 0, 0,},
      {0, 0, 0, 0, 0, 0, 8, 9, 0,},
      {0, 0, 3, 0, 9, 0, 0, 6, 0,},
      {4, 2, 7, 0, 0, 0, 5, 8, 9,},
      {0, 6, 0, 0, 8, 0, 2, 0, 0,},
      {0, 7, 2, 0, 0, 0, 0, 0, 0,},
      {0, 0, 4, 5, 7, 6, 3, 2, 0,},
      {6, 3, 0, 0, 0, 0, 7, 0, 4,},
    };

    //int grid[N][N] = {
    //  {0, 0, 0, 1, 2, 0, 0, 3, 0,},
    //  {0, 0, 3, 0, 8, 0, 0, 1, 6,},
    //  {4, 0, 0, 5, 3, 0, 0, 9, 0,},
    //  {0, 1, 0, 8, 0, 0, 5, 2, 0,},
    //  {0, 4, 0, 0, 0, 0, 0, 6, 0,},
    //  {0, 6, 8, 0, 0, 2, 0, 7, 0,},
    //  {0, 8, 0, 0, 9, 3, 0, 0, 2,},
    //  {6, 9, 0, 0, 5, 0, 3, 0, 0,},
    //  {0, 3, 0, 0, 4, 8, 0, 0, 0,},
    //};

    //int grid[N][N] = {
    //  {6, 0, 0, 8, 0, 9, 0, 0, 0,},
    //  {0, 0, 5, 0, 0, 7, 0, 8, 6,},
    //  {0, 7, 0, 0, 0, 0, 0, 0, 0,},
    //  {0, 0, 0, 4, 0, 1, 3, 0, 7,},
    //  {8, 0, 1, 0, 0, 0, 5, 0, 4,},
    //  {7, 0, 9, 2, 0, 5, 0, 0, 0,},
    //  {0, 0, 0, 0, 0, 0, 0, 4, 0,},
    //  {1, 8, 0, 5, 0, 0, 6, 0, 0,},
    //  {0, 0, 0, 3, 0, 4, 0, 0, 5,},
    //};

    //int grid[N][N] = {
    //  {1, 0, 0, 0, 0, 0, 0, 0, 0,},
    //  {7, 0, 0, 0, 0, 8, 1, 0, 2,},
    //  {0, 6, 3, 0, 5, 0, 0, 0, 0,},
    //  {0, 7, 0, 3, 9, 0, 0, 0, 0,},
    //  {0, 0, 5, 8, 0, 4, 6, 0, 0,},
    //  {0, 0, 0, 0, 2, 5, 0, 4, 0,},
    //  {0, 0, 0, 0, 1, 0, 8, 7, 0,},
    //  {2, 0, 8, 9, 0, 0, 0, 0, 3,},
    //  {0, 0, 0, 0, 0, 0, 0, 0, 6,},
    //};

    int rows[N];
    int cols[N];
    int boxes[N];

    for(int i = 0; i < N; ++i) {
      rows[i] = cols[i] = boxes[i] = 1;
    }

    vector<pair<int, int> > emptys;
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < N; ++j) {
        if(grid[i][j] == 0) {
          emptys.push_back(pair<int, int>(i, j));
        } else {
          int d = IDX_TO_PRIME[grid[i][j] - 1];
          rows[i] *= d;
          cols[j] *= d;
          boxes[i - i % 3 + j / 3] *= d;
        }
      }
    }
    if(solve(grid, rows, cols, boxes, emptys)) {
      //printGrid(grid);
      times[count++] = (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000);
    } else {
      //cout << "NO SOLUTION FOUND!" << endl;
    }
  }

  double sum = std::accumulate(std::begin(times), std::end(times), 0.0);
  double m =  sum / times.size();

  double accum = 0.0;
  std::for_each (std::begin(times), std::end(times), [&](const double d) {
      accum += (d - m) * (d - m);
  });

  double stdev = sqrt(accum / (times.size()-1));

  cout << nums << " iterations done." << endl;
  cout << m << ' ' << stdev << endl;
  return 0;
}

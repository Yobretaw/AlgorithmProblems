#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_set>
#include <utility>
#include <ctime>
#include <numeric>
#include <queue>
#include <cstdlib>
using namespace std;

int INT_MAX = 1 << 31 - 1;
int INT_MIN = -1;

#define N 9
#define ENABLE_FORWARD_CHECKING 0
#define MCDV 0
#define MCGV 0
#define LCGV 0

long long g_num_nodes = 0;

bool isSafe(int su[N][N], int row, int col, int num, long long  rows[N], long long  cols[N], long long  boxes[N]);
bool findUassignedLocation(int su[N][N], int& row, int& col, vector<pair<int, int> >& emptys);
bool solve(int su[N][N], long long rows[N], long long cols[N], long long boxes[N], vector<pair<int, int> >& emptys);
void printGrid(int grid[N][N]);
bool isValidSudoku(int grid[N][N]);
int random_generator(int i);
bool forwardChecking(int grid[N][N], int i, int j, long long rows[N], long long cols[N], long long boxes[N]);


// Global variables
int GLOBAL_COUNT = 0;
int IDX_TO_PRIME[9] = {2, 3, 5, 7, 11, 13 ,17, 19, 23};
int PRIME_PRODUCT = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23;
vector<int> random_idx = {1, 2, 3, 4, 5, 6, 7, 8, 9};

bool isSafe(
    int su[N][N],
    int row,
    int col,
    int num,
    long long  rows[N],
    long long  cols[N],
    long long  boxes[N])
{

  num = IDX_TO_PRIME[num - 1];
  return rows[row] % num != 0 && cols[col] % num != 0 && boxes[row - row % 3 + col / 3] % num != 0;
}

bool findUassignedLocation(
    int su[N][N],
    int& row,
    int& col,
    vector<pair<int, int> >& emptys)
{
  // no empty slot
  if(emptys.empty()) return false;

  // Most Constrained Variable
  if(MCDV) {
    vector<int> rows(N);
    vector<int> cols(N);
    vector<int> boxes(N);

    for(auto v : emptys) {
      rows[v.first] += 1;
      cols[v.second] += 1;
      boxes[v.first - v.first % 3 + v.second / 3] += 1;
    }

    int max_val = INT_MIN;
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < N; ++j) {
        int curr = rows[i] + cols[j] + boxes[i - i % 3 + j / 3];
        if(su[i][j] == 0 && curr > max_val) {
          row = i;
          col = j;
          max_val = curr;
        }
      }
    }
  } else if(MCGV) {
    // Most Constraining Variable
    vector<int> rows(N);
    vector<int> cols(N);
    vector<int> boxes(N);

    for(auto v : emptys) {
      rows[v.first] += 1;
      cols[v.second] += 1;
      boxes[v.first - v.first % 3 + v.second / 3] += 1;
    }

    int max_count = INT_MAX;
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < N; ++j) {
        int curr = rows[i] + cols[j] + boxes[i - i % 3 + j / 3];
        if(su[i][j] == 0 && curr < max_count) {
          row = i;
          col = j;
          max_count = curr;
        }
      }
    }
  } else if(LCGV) {
    // Least Constraining Variable
    vector<int> rows(N);
    vector<int> cols(N);
    vector<int> boxes(N);

    for(auto v : emptys) {
      rows[v.first] += 1;
      cols[v.second] += 1;
      boxes[v.first - v.first % 3 + v.second / 3] += 1;
    }

    int max_count = INT_MAX;
    for(int i = 0; i < N; ++i) {
      for(int j = 0; j < N; ++j) {
        int curr = rows[i] + cols[j] + boxes[i - i % 3 + j / 3];
        if(su[i][j] == 0 && curr < max_count) {
          row = i;
          col = j;
          max_count = curr;
        }
      }
    }
  }

  // Heuristics enabled
  if(MCDV || MCGV || LCGV) {
    int idx = 0;
    for(auto it = emptys.begin(); it != emptys.end(); ++it) {
      if(it->first == row && it->second == col) {
        emptys.erase(it);
        emptys.push_back(pair<int, int>(row, col));
        break;
      }
    }
  } else {
    row = emptys[emptys.size() - 1].first;
    col = emptys[emptys.size() - 1].second;
  }
  return true;
}

bool solve(
    int su[N][N],
    long long  rows[N],
    long long  cols[N],
    long long  boxes[N],
    vector<pair<int, int> >& emptys)
{
  g_num_nodes += 1;
  int row, col;
  if(!findUassignedLocation(su, row, col, emptys)) {
    return true;
  }

  emptys.pop_back();

  // always randomly shuffle the number to be tried next
  //random_shuffle(random_idx.begin(), random_idx.end());
  //next_permutation(random_idx.begin(), random_idx.end());

  for (auto i : random_idx) {
    if(isSafe(su, row, col, i, rows, cols, boxes)) {
      su[row][col] = i;

      int d = IDX_TO_PRIME[i - 1];
      rows[row] *= d;
      cols[col] *= d;
      boxes[row - row % 3 + col / 3] *= d;

      if(ENABLE_FORWARD_CHECKING && !forwardChecking(su, row, col, rows, cols, boxes)) {
        // there is a slot that no values can be assigned to it without confictling to others
        rows[row] /= d;
        cols[col] /= d;
        boxes[row - row % 3 + col / 3] /= d;
        su[row][col] = 0;
        continue;
      }

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

bool forwardChecking(
    int grid[N][N],
    int row,
    int col,
    long long  rows[N],
    long long  cols[N],
    long long  boxes[N])
{
  // row/col check
  for(int i = 0; i < N; ++i)
    if((grid[row][i] == 0 && (rows[row] * cols[i]) % PRIME_PRODUCT == 0)
        || (grid[i][col] == 0 && (rows[i] * cols[col]) % PRIME_PRODUCT == 0)) {
      return false;
    }

  // box check: only needs to check four corner slots since others
  // have been examed in row/col check
  int box_val = boxes[row - row % 3 + col / 3];
  int i = row - row % 3;
  int j = col - col % 3;
  int x, y;
  for(int a = 0; a <= 2; a += 2) {
    for(int b = 0; b <= 2; b += 2) {
      x = i + a;
      y = j + b;
      if(grid[x][y] == 0 && ((rows[x] * cols[y] * box_val) % PRIME_PRODUCT == 0)) {
        return false;
      }
    }
  }
  return true;
}

void printGrid(int grid[N][N]) {
    for (int row = 0; row < N; row++)
    {
       for (int col = 0; col < N; col++)
             printf("%2d", grid[row][col]);
        printf("\n");
    }
}


bool isValidSudoku(int grid[N][N]) {
  long long rows[N]; 
  long long cols[N]; 
  long long boxes[N]; 
  for(int i = 0; i < N; ++i) {
    rows[i] = cols[i] = boxes[i] = 1;
  }
  for(int i = 0; i < N; ++i) {
    for(int j = 0; j < N; ++j) {
      int d = IDX_TO_PRIME[grid[i][j] - 1];
      if(rows[i] % d == 0 || cols[j] % d == 0 || boxes[i - i % 3 + j / 3] % d == 0){
        return false;
      }
      rows[i] *= d;
      cols[j] *= d;
      boxes[i - i % 3 + j / 3] *= d;
    }
  }
  return true;
}

int main(int argc, const char *argv[])
{
  int count = 0;
  int nums = 2;
  vector<long long> times(nums);
  for(int i = 0; i < nums; ++i) {
    clock_t start = clock();

    // EASY :)
    //int grid[N][N] = {
    //  {3, 0, 9, 0, 0, 0, 0, 4, 2,},
    //  {0, 1, 8, 9, 4, 3, 6, 0, 0,},
    //  {0, 0, 0, 0, 0, 0, 8, 9, 0,},
    //  {0, 0, 3, 0, 9, 0, 0, 6, 0,},
    //  {4, 2, 7, 0, 0, 0, 5, 8, 9,},
    //  {0, 6, 0, 0, 8, 0, 2, 0, 0,},
    //  {0, 7, 2, 0, 0, 0, 0, 0, 0,},
    //  {0, 0, 4, 5, 7, 6, 3, 2, 0,},
    //  {6, 3, 0, 0, 0, 0, 7, 0, 4,},
    //};

    // MEDIUM :/
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

    // HARD :(
    int grid[N][N] = {
      {6, 0, 0, 8, 0, 9, 0, 0, 0,},
      {0, 0, 5, 0, 0, 7, 0, 8, 6,},
      {0, 7, 0, 0, 0, 0, 0, 0, 0,},
      {0, 0, 0, 4, 0, 1, 3, 0, 7,},
      {8, 0, 1, 0, 0, 0, 5, 0, 4,},
      {7, 0, 9, 2, 0, 5, 0, 0, 0,},
      {0, 0, 0, 0, 0, 0, 0, 4, 0,},
      {1, 8, 0, 5, 0, 0, 6, 0, 0,},
      {0, 0, 0, 3, 0, 4, 0, 0, 5,},
    };

    // EVIL ::>_<::
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

    g_num_nodes = 0;

    long long  rows[N];
    long long  cols[N];
    long long  boxes[N];

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

    // random variable order
    random_shuffle(emptys.begin(), emptys.end());
    //next_permutation(emptys.begin(), emptys.end());

    // random value order
    random_shuffle(random_idx.begin(), random_idx.end());
    if(solve(grid, rows, cols, boxes, emptys)) {
      //cout << i << endl;
      //times[count++] = (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000);
      times[count++] = g_num_nodes;
      //printGrid(grid);
      //cout << isValidSudoku(grid) << endl;
    } else {
      cout << "NO SOLUTION FOUND!" << endl;
    }
  }
  for(auto v : times) cout << v << endl;
  // compute average run time & their standard devaition
  long long sum = std::accumulate(std::begin(times), std::end(times), 0);
  long long m =  sum / times.size();
  cout << m << endl;
  long long accum = 0;
  std::for_each (std::begin(times), std::end(times), [&](const long long d) {
      accum += (d - m) * (d - m);
  });

  long long stdev = sqrt(accum / (times.size() == 1 ? 1 : times.size()-1));

  cout << nums << " iterations done." << endl;
  cout << "Average nodes: " << m << ". \nStandard devaition: " << stdev << "." << endl;
  return 0;
}

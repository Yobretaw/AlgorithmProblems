#include "iostream"
#include "stdlib.h"
using namespace std;

// mx is a matrix with m rows and n columns
void setToZero(int** mx, int m, int n) {
  int* rows = new int[m];
  int* cols = new int[n];

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if(mx[i][j] ==0) {
        rows[i] = 1;
        cols[j] = 1;
      }
    }
  }

  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if(rows[i] == 1 || cols[j] == 1)
        mx[i][j] = 0;
    }
  }

  delete rows;
  delete cols;
}

int main()
{
  //...
  return 0;
}

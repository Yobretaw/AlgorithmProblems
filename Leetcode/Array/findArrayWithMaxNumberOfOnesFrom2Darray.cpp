#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
using namespace std;

// A row and column wise 2d sorted array is given which only contains 0s and 1s in each row.
// Find the row which is having maximum number of ones.
// return the index of array with most number of ones
int find(const vector<vector<int> >& m) {
  int numZero = 0;
  int maxIdx = 0;

  for (int i = 0; i < (int)m[0].size(); ++i) {
    if(m[0][i] == 1)
      break;
    numZero++;
  }

  for (int i = 1; i < (int)m.size(); ++i) {
    int curr = numZero;
    while(m[i][curr-1] == 1 && curr >= 1)
      curr--;

    if(curr < numZero) {
      maxIdx = i;
      numZero = curr;
    }
  }

  return maxIdx;
}

int main() {
  vector<int> v1 = {0, 0, 1, 1, 1};
  vector<int> v2 = {0, 1, 1, 1, 1};
  vector<int> v4 = {0, 0, 0, 1, 1};
  vector<int> v3 = {1, 1, 1, 1, 1};
  vector<vector<int> > m = {v1, v2, v3, v4};
  cout << find(m) << endl;
  return 0;
}

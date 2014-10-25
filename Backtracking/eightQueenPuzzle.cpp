#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

#define N 8

bool isSafe(int current_row, int col, vector<int>& pos) {
  for (int other_row = 0; other_row < current_row; other_row++) {
    int other_col = pos[other_row];

    if(other_col == col || //same col
        other_col == col - (current_row - other_row) || // same diagonal
        other_col == col + (current_row - other_row)) // same diagonal
      return false;
  }

  return true;
}

void print(const vector<int>& pos) {
  static int count = 0;
  count++;
  // pos[i] = j represents that the queen in ith row is in jth column
  cout << "Solution #" << count << ": " << endl;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if(pos[i] == j)
        cout << "Q" << " ";
      else
        cout << "." << " ";
    }
    cout << endl;
  }
  cout << endl;
}

void solve(int row, vector<int>& pos) {
  if(row == N) {
    print(pos);
    return;
  }

  for (int i = 0; i < N; i++) {
    if(isSafe(row, i, pos)) {
      pos[row] = i;
      solve(row+1, pos);
    }
  }
}

int main()
{
  vector<int> a(N);
  solve(0, a);
  return 0;
}

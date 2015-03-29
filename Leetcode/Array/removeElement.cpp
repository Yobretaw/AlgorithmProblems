#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_map>
using namespace std;

// Given an array and a value, remove all instances of that
// value in place and return the new length
int removeElements(int A[], int len, int val) {
  int idx = 0;
  for(int i = 0; i < len; i++) {
    if(A[i] == val) continue;

    A[idx++] = A[i];
  }

  return idx;
}

int main() {
  int A[] = { 1, 1, 2, 3, 5, 3, 2, 1, 5, 6 };
  int len = removeElements(A, 10, 3);
  for (int i = 0; i < len; ++i) {
    cout << A[i] << endl;
  }
  return 0;
}

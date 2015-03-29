#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <unordered_map>
using namespace std;

// if the sum of integers in a overflows, this algorithm
// won't work;
int findMissingNumber(const vector<int>& a) {
  int n = a.size();

  int total = (n * (n + 1)) / 2;
  for (int i = 0; i < a.size(); ++i) {
    total -= a[i];
  }
  return total;
}

// works even if sum overflows
int findMissingNumber2(const vector<int>& a) {
  int n = a.size();
  int x1 = 0, x2 = 0;
  for (int i = 0; i < n; ++i) {
    x1 ^= a[i];
    x2 ^= (i + 1);
  }
  x2 ^= (n + 1);
  return x1 ^ x2;
}

int main() {
  vector<int> a = {1, 3, 5, 4, 2, 7};
  cout << findMissingNumber2(a) << endl;
  return 0;
}

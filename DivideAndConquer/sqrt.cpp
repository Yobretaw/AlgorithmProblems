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

int sqrt2(int x) {
  int left = 1, right = x / 2;
  int last_mid;

  if(x < 2) return x;

  while(left <= right) {
    int mid = left + (right - left) / 2;
    if(x / mid > mid) {   // don't use x > mid * mid to avoid overflow
      left = mid + 1;
      last_mid = mid;
    } else if(x / mid < mid) {
      right = mid - 1;
    } else {
      return mid;
    }
  }
  return last_mid;
}

int main() {
  cout << sqrt2(2000) << endl;
  return 0;
}

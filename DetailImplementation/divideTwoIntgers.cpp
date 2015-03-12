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

/*
 *  Divide two integers without using multiplication, division and mod operator.
 *  
 *  If it is overflow, return MAX_INT.
 */
int divide(int dividend, int divisor) {
  // when dividend equals INT_MIN, -dividend will overflow, hence we use long long here
  long long a = dividend >= 0 ? dividend : -(long long)dividend;
  long long b = divisor >= 0 ? divisor : -(long long)divisor;

  // when dividend = INT_MIN and divisor = -1, the result will overflow, so use long long
  long long result = 0;
  while(a >= b) {
    long long c = b;
    int i = 0;
    while(a >= c) {
      a -= c;
      result += 1 << i;
      i++;
      c <<= 1;
    }
  }
  return ((dividend^divisor) >> 31) ? -result : result;
}

int main() {
  cout << divide(1008012320, 33) << endl;
  return 0;
}
